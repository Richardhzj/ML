function [frames,timeline] = preProcess(wav,fs,winLen,overLap,name)
%PREPROCESS �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
disp(['���ڶ���Ƶ',name,'��ǰ������']);
if fs~=48000
    wav = resample(wav,48000,fs);
end
[~,n] = size(wav);
if n == 2
    wav = (wav(:,1)+wav(:,2))/2;
end

winLen = round(winLen*48);
overLap = round(overLap*winLen);
[frames,timeline] = enframe(wav,winLen,overLap);
timeline = round(timeline/fs,4);
end


