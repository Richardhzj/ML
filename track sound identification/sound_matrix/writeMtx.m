function [] = writeMtx(output,outputPath,name)
%WRITEMTX �˴���ʾ�йش˺�����ժҪ
le = length(name);
for lop = 1:4
    if isempty(output{lop}{2})
        continue;
    end
    op = [outputPath,name(1:le-4),output{lop}{1},'.csv'];
    disp(['����д����Ƶ',name,'��',output{lop}{1},'���������ļ�']);
    res = output{lop}{2};
    disp(size(res))
    csvwrite(op,res);

end
end

