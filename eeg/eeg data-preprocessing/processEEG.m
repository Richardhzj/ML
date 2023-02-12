% s=0;
% a=[12,13,14;15,16,17;18,19,20;21,22,23];
% for k=a
%     s=s+k;
% end
% disp(s');


% a = [1,1,1,2,2,2,3,3,3,4,4,4];
% b = [];
% for i = 1:4
%     b1 = mean(a((3*i-2):3*i));
%     b=[b b1];
% end;
% disp(b)
% namelist = dir('C:\Users\richard\Box\Computer Science EEG study\*.dap');
% len = length(namelist);
% for i = 1:len
%   disp(namelist(i).name(1:length(namelist(i).name)-4));
% end;
% for file = namelist
%     disp(file.name);
% end;


% a = [1,2,3,4,5];
% for i = a
%     disp(i);
% end;
% 
% abcd =[1,1,2,2,3,3;4,4,5,5,6,6;7,7,8,8,9,9];
% meanArray = [];
% for i = 1:3
% tmp = mean(abcd(:,(2*i-1):2*i),2);
% meanArray=[meanArray tmp];
% end;
% 
% stdArray = [];
% for i = 1:3
% disp(abcd(:,(2*i-1):2*i));
% tmp = std(abcd(:,(2*i-1):2*i),0,2);
% 
% stdArray=[stdArray tmp];
% end;


%---
data = readmatrix("beforeQuantizHealthy.csv");
partition = -54388:7:132496;
partition(end+1) = 132496;
codebook = 200:26899;
[r,c] = size(data);

for i = 1:r
   [index,quantized]= quantiz(data(i,:),partition,codebook);
   data(i,:) = quantized;
end

writematrix(data,'afterQuantizHealthy.csv') 
% 
% 
% 
% partition = -38604:2:17153;
% partition(end+1) = 17153;
% codebook = 200:28081;
% quantiz([-38604,17150,17152,17153],partition,codebook)
% %---
% 
% partition = [-10,-9,3];
% codebook = [200,201,202,203];
% [index,quants] = quantiz([-10 -5 4],partition,codebook)