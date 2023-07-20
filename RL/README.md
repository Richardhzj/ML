### 一、下载Conda

首先应该下载”miniconda“，Conda是一个开源的软件包管理系统和环境管理系统，可以运行在Windows、macOS和Linux等操作系统上。它可以快速安装、运行和更新软件包及其依赖项，也可以轻松地在本地计算机上创建、保存、加载和切换环境。虽然最初被设计用于Python程序，但Conda实际上可以封装和分发任何软件。

https://docs.conda.io/en/latest/miniconda.html

下载完成之后并且成功改变环境变量之后

```
conda create -n tbs python=3.10
```

如果pip下载包的速度过慢可以更换下载源，pip更换为国内镜像源，例如阿里云的镜像源

```
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
```

conda删除环境

```
conda remove -n tbs --all
```

conda激活环境

```
conda activate tbs
```

conda退出环境

```text
conda deactivate
```

### 二、下载第三方模块

首先激活tbs环境，导入模块

```
conda activate tbs
```

#### 下列模块为算法必须的模块

tensorflow：https://pypi.org/project/tensorflow/

```
pip install tensorflow
```

stable-baselines3 ：https://pypi.org/project/stable-baselines/

```
pip install stable-baselines3
```

mysql库

```
pip install mysql-connector-python
```

注意下列安装的pytorch为cuda版本，请去pytorch下载对应电脑的版本，下载cuda版本的pytorch前请先卸载之前的pytorch。https://pytorch.org/

```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

#### 下列模块为与Unreal连接所必须的模块

Flask：https://pypi.org/project/Flask/

```
pip install Flask
```

Eventlet：https://pypi.org/project/eventlet/

```
pip install eventlet
```

Engineio：https://pypi.org/project/python-engineio/

```
pip install python-engineio
```

SocketIO：https://pypi.org/project/python-socketio/

```
pip install python-socketio
```

### 三、训练参数说明

- `ep_len_mean`：平均回合长度（Episode Length），表示训练期间每个回合的平均步数。

- `ep_rew_mean`：平均回合奖励（Episode Reward），表示每个回合的平均奖励值。

- `approx_kl`：提前停止训练的近似反向KL散度（Approximate Reverse KL Divergence），近似反向KL散度被用作训练过程中的早停准则。当近似反向KL散度超过预设的目标值时，表明新策略与旧策略之间的差异较大，可能会导致不稳定的训练或性能下降，因此提前停止训练以避免继续训练可能带来的负面影响。KL 散度接近零说明模型拟合效果较好。

  ```python
  # Calculate approximate form of reverse KL Divergence for early stopping
  # see issue #417: https://github.com/DLR-RM/stable-baselines3/issues/417
  # and discussion in PR #419: https://github.com/DLR-RM/stable-baselines3/pull/419
  # and Schulman blog: http://joschu.net/blog/kl-approx.html
  with th.no_grad():
      log_ratio = log_prob - rollout_data.old_log_prob
      approx_kl_div = th.mean((th.exp(log_ratio) - 1) - log_ratio).cpu().numpy()
      approx_kl_divs.append(approx_kl_div)
  
  if self.target_kl is not None and approx_kl_div > 1.5 * self.target_kl:
      continue_training = False
      if self.verbose >= 1:
          print(f"Early stopping at step {epoch} due to reaching max kl: {approx_kl_div:.2f}")
  	break
  ```

- `clip_fraction`：剪切比例表示被剪切的更新步骤所占的比例，即更新步骤中因为超过了剪切范围而被剪切的比例。通过监控和记录剪切比例，可以评估剪切操作对更新步骤的影响程度，以及算法的稳定性和收敛性。梯度剪枝的目的是为了防止梯度过大导致的不稳定性，但过多的剪枝也会影响模型的训练效果。一般来说，剪枝系数越小越好。

  ```python
  clip_fraction = th.mean((th.abs(ratio - 1) > clip_range).float()).item()
  clip_fractions.append(clip_fraction)
  ```

  `ratio` 是新策略概率（probability of new policy）与旧策略概率（probability of old policy）的比值

- `clip_range`：剪切范围是一种用于控制策略梯度更新的方法，在 Proximal Policy Optimization (PPO) 等算法中经常被使用。它用于限制每次更新中策略梯度的变化范围，控制模型更新过程中的不会大幅度变化，防止更新过程过于激进。根据训练进度的剩余比例，可以动态地调整剪切范围，使得剪切范围随着训练的进行逐渐减小，从而更好地控制训练的稳定性和收敛性。

  超参数中`clip_range`剪枝范围指定了对梯度进行剪枝的上下限值，其大小影响梯度剪枝的幅度。如果剪枝范围设置不当，过大或者过小，都会影响模型的训练效果和稳定性。

- `entropy_loss`：熵损失（Entropy Loss），熵是信息理论中的一个概念，用于度量概率分布的不确定性。在强化学习中，熵常被用作一种探索项，以鼓励策略在选择动作时保持多样性，从而促进探索。通过最大化熵损失，可以增加策略产生更加多样化的动作，从而降低策略陷入局部最优解的风险，有助于在策略搜索空间中找到更好的解决方案。熵损失越小，说明模型的预测更加准确，这对于强化学习任务的成功非常重要。

  如果entropy loss的值为负数，那么说明当前策略的动作分布过于集中或确定性，缺乏探索性。这可能导致策略陷入局部最优，无法发现更好的策略。

  为了解决这个问题，可以考虑增加entropy loss的权重或调整策略网络的架构，以提高探索性并增加策略的多样性。增加entropy loss的权重将使其在总体损失函数中占据更重要的比重，从而促使策略更加探索性。

- `explained_variance`：解释方差是用来度量值函数估计器的性能的指标之一。它衡量了值函数对于实际回报的解释能力，即值函数对于回报的变异性有多少解释能力。解释方差的取值范围在[-1, 1]之间，越接近1表示值函数的预测与实际回报的相关性越强，性能越好。如果解释方差为负或接近零，则表示值函数的预测性能较差。具体地说，如果解释方差为1，说明预测值完全准确；如果解释方差为0，则意味着预测值与真实值没有任何相关性；如果解释方差为负数，则说明模型表现得比随机猜测还要差。

- `learning_rate`：学习率决定了每次更新模型参数的步长，过大或过小都会影响训练效果和稳定性。通常需要通过调参来确定一个适合模型的学习率。

- `loss`：总体损失是指模型的损失函数在当前训练批次中的平均值，用于评估模型的性能和效果。如果训练过程中 loss 比较小，则说明模型的泛化能力和预测准确性比较好。

  ```python
  loss = policy_loss + self.ent_coef * entropy_loss + self.vf_coef * value_loss
  ```

  计算了总体损失（Loss），该损失由三部分组成：策略损失（policy_loss）、熵损失（entropy_loss）和值函数损失（value_loss）。

  上述三部分损失分别乘以权重系数（`self.ent_coef` 和 `self.vf_coef`），然后相加得到总体损失。

- `n_updates`：更新次数是指模型在当前训练批次中参数更新的次数，对模型效果的影响与学习率和样本批次大小等因素有关。

- `policy_gradient_loss`：策略梯度损失是指由于不断迭代优化策略而产生的损失，这个损失决定了策略梯度算法的收敛速度和效果。一般来说，策略梯度损失越小，模型的表现就越好。

  修剪后的近似损失是 PPO 算法中常用的损失函数。它通过限制更新步长，避免更新策略过于剧烈，同时保留一些原始的梯度信息，有助于更稳定地训练策略网络。此方式可以提高算法的鲁棒性，避免陷入局部最优解并更好地探索策略搜索空间。

  ```python
  # clipped surrogate loss
  policy_loss_1 = advantages * ratio
  policy_loss_2 = advantages * th.clamp(ratio, 1 - clip_range, 1 + clip_range)
  policy_loss = -th.min(policy_loss_1, policy_loss_2).mean()
  
  # Logging
  pg_losses.append(policy_loss.item())
  ```

- `std`：标准差是指样本数据集中各数据点与平均值之间的偏离程度的平方根，标准差越小说明数据集中的数据分布越紧密，相反则说明数据分布越分散，这会影响模型的泛化能力。

- `value_loss`：表示使用 TD(gae_lambda) 目标计算的值函数损失（Value Function Loss）。该损失用于衡量实际回报（returns）和值函数预测值（values_pred）之间的均方误差（Mean Squared Error）。在强化学习中，价值函数用于评估每个状态的价值，从而指导智能体的行动，与策略梯度算法一起构成了强化学习的两个主要组件。价值损失越小，说明模型对于每个状态的价值估计更加准确。

  ```python
  if self.clip_range_vf is None:
      # No clipping
      values_pred = values
  else:
      # Clip the difference between old and new value
      # NOTE: this depends on the reward scaling
      values_pred = rollout_data.old_values + th.clamp(
      values - rollout_data.old_values, -clip_range_vf, clip_range_vf
      )
  # Value loss using the TD(gae_lambda) target
  value_loss = F.mse_loss(rollout_data.returns, values_pred)
  value_losses.append(value_loss.item())
  ```

  

