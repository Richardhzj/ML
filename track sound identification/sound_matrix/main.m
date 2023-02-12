clear;
clc;
close all;
%===================↓↓↓参数设置，请根据实际情况修改↓↓↓==============
dataPath = 'D:\data\sound\errorSound\';                        %数据文件夹内只能是音频文件，不可以出现其他文件和文件夹
outputPath = 'D:\data\soundFeatureMatrixError\';%必须提前建立文件夹，注意检查路径字符，不要出错
winLen = 50;%每个分析帧的时间长度，单位毫秒。建议设置为在区间[10,1000]内
overLap = 0.5;%每两个分析帧的重叠长度，单位比例1。建议设置为在区间 [0.2,0.8] 内
%===================↑↑↑参数设置，请根据实际情况修改↑↑↑==========
if ~exist(outputPath,'dir')
    mkdir(outputPath)
end

%=============↓↓↓输出特征设置，要进行输出的设为1↓↓↓=============
STFT_Amp = 1; %短时傅里叶幅度谱特征矩阵
STFT_Phs = 1;  %短时傅里叶相位谱特征矩阵
SPCT_Org = 1;  %功率谱密度特征矩阵
SPCT_Log = 1;  %对数功率谱密度特征矩阵
%=============↑↑↑把不需要输出的特征设为0，可以提高运行速度↑↑↑================

options = [STFT_Amp,STFT_Phs,SPCT_Org,SPCT_Log];
allData = dir(dataPath);
allData(1:2) = [];
for lop = 1:length(allData)
    [wav,fs] = audioread([dataPath,allData(lop).name]);
    [frames,timeLine] = preProcess(wav,fs,winLen,overLap,allData(lop).name);
    output = postProcess(frames,48000,winLen,overLap,options,allData(lop).name);
    writeMtx(output,outputPath,allData(lop).name);
end

%[m,n] =size(frames);

%freqLine = linspace(0,fs/2-1000/winLen,round(n/2));
% TFwav = zeros(m,n);
% for lop = 1:m
%     TFwav(lop,:) = fft(frames(lop,:));
% end

