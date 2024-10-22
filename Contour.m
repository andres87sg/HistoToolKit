% Crea el contorno de la máscara sobre la imágen en RGB

close all;
clear;
clc;

im1 = imread('D:\JournalPaper_Experiments\IvyGap+TCGA\PC_1792_raw\Training\PC\TCGA-02-0015_002.jpg');
mask = imread('D:\JournalPaper_Experiments\IvyGap+TCGA\PC_1792_raw\Training\PC_SG\SG_TCGA-02-0015_002.jpg');

% im1 = imread('D:\GBM_Project\Current_Experiments\MV_Patches\MV_896_raw\Testing\MV\W9-1-1-H.2.01_0014_MV.jpg');
% mask = imread('D:\GBM_Project\Current_Experiments\MV_Patches\MV_896_ChA_data_augm\Testing\MV_SG2\SG_W9-1-1-H.2.01_0014_MV.jpg');

mask_boundaries = bwboundaries(mask(:,:,1));

figure, 
subplot(1,3,1);

% imshow(im1);
% title('H&E')
% subplot(1,3,2);
% imshow(mask);
% title('Prediction')
% subplot(1,3,3);
% imshow(im1);
% title('Prediction')
% hold on;

subplot(1,2,1);
imshow(im1);
title('H&E')
% imshow(mask);
% title('Prediction')
subplot(1,2,2);
imshow(im1);
title('Prediction')
hold on;

numVascMask = size(mask_boundaries,1);

for i=1:numVascMask
    b = mask_boundaries{i};
    plot(b(:,2),b(:,1),'.r');    
end
