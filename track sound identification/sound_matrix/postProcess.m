function [output] = postProcess(frames,fs,winLen,overLap,options,name)
    disp(['���������Ƶ',name,'��ȫ����������']);
    [m,n] =size(frames);
    if mod(n,2)==1
        error('ʱ��֡�����������������㣬����������winLen��overLap��ֵ(������Ҫȡ����С��)');
    end
    if sum(options) == 0
         error('������ѡ�����һ������');
    end
    res = [];
    output = {{'STFT_Amp',res},{'STFT_Phs',res},{'SPCT_Org',res},{'SPCT_Log',res}};
%     k = 1000/winLen;
    
    TFwav = zeros(m,n);
    for lop = 1:m
        TFwav(lop,:) = fft(frames(lop,:));
    end

    if options(1)
          res = abs(TFwav)/(fs/2);  
          output{1}{2} = res(:,1:end/2+1);
    end

    if options(2)
          res = angle(TFwav);
          output{2}{2} =  res(:,1:end/2+1);
    end
     wl = winLen/1000*fs;
    op = wl*overLap;
    res = zeros(m,n/2+1);
    if options(3)&&options(4)
            for lop = 1:m
                res(lop,:) =  pwelch(frames(lop,:),wl,op,wl,fs);
            end
             output{3}{2} = res;
             res = 10*log10(res/max(res(:)));
             output{4}{2} = res;
    else
        if options(4)
            for lop = 1:m
                res(lop,:) =  pwelch(frames(lop,:),wl,op,wl,fs);
            end
             res = 10*log10(res/max(res(:)));
             output{4}{2} = res;
        else
            if options(3)
                for lop = 1:m
                    res(lop,:) =  pwelch(frames(lop,:),wl,op,wl,fs);
                end
             output{3}{2} = res;
            end
        end
    end



end

