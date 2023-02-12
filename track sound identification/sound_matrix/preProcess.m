function [frames,timeline] = preProcess(wav,fs,winLen,overLap,name)
%PREPROCESS 此处显示有关此函数的摘要
%   此处显示详细说明
disp(['正在对音频',name,'做前处理处理']);
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


