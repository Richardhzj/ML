function [] = writeMtx(output,outputPath,name)
%WRITEMTX 此处显示有关此函数的摘要
le = length(name);
for lop = 1:4
    if isempty(output{lop}{2})
        continue;
    end
    op = [outputPath,name(1:le-4),output{lop}{1},'.csv'];
    disp(['正在写入音频',name,'的',output{lop}{1},'特征矩阵文件']);
    res = output{lop}{2};
    disp(size(res))
    csvwrite(op,res);

end
end

