import shutil
import os, sys
import random

if __name__ == '__main__':
    rootPath='./Images'
    if not os.path.isdir(rootPath):
        exit()
    clusterDirs = os.listdir(rootPath)
    
    labelMapCluster = dict()
    trainList = dict()
    validList = dict()
    testList = dict()
    allList =dict()

    for idx, clusterName in enumerate(clusterDirs):
        labelMapCluster[clusterName] = idx
        
        clusterPath = os.path.join(rootPath, clusterName)
        files = os.listdir(clusterPath)
        random.shuffle(files)

        filenum = len(files)
        n=300
        if filenum<n:
            n = filenum
        k =0
        for i, image in enumerate(files):
            newimage = image
            if 'gif' in image:
                continue
            if ' ' in image:
                newimage=image.replace(" ","_");
                os.rename(os.path.join(clusterPath, image), os.path.join(clusterPath, newimage))
            strs = clusterName + '/' + newimage
            strs=strs.replace(" ","_");
#            allList[strs] = idx
            if k<n*0.8:
                trainList[strs] = idx
            elif (k<n*0.95):
                validList[strs] = idx
            else:
                testList[strs] = idx
            k=k+1

#    allList = sorted(allList.items(), key=lambda x: x[1])
#    with open('allImagehhh.txt', 'w') as f:
#        f.write('\n'.join('%s %d' % x for x in allList))

    labelMapCluster = sorted(labelMapCluster.items(), key=lambda x: x[1])
    trainList = sorted(trainList.items(), key=lambda x: x[1])
    validList = sorted(validList.items(), key=lambda x: x[1])
    testList = sorted(testList.items(), key=lambda x: x[1])
    print(len(trainList))
    print(len(validList))
    with open('new_map.txt', 'w') as f:
        f.write('\n'.join('%s\t%s' % x for x in labelMapCluster))
#        f.writelines('{}\t{}\n'.format(k,v) for k,v in labelMapCluster.items())
    with open('new_train.txt', 'w') as f:
        f.write('\n'.join('%s %d' % x for x in trainList))
#        f.writelines('{}\t{}\n'.format(k,v) for k,v in trainList.items())
    with open('new_valid.txt', 'w') as f:
        f.write('\n'.join('%s %d' % x for x in validList))
#        f.writelines('{}\t{}\n'.format(k,v) for k,v in validList.items())
    with open('new_test.txt', 'w') as f:
        f.write('\n'.join('%s %d' % x for x in testList))
#        f.writelines('{}\t{}\n'.format(k,v) for k,v in validList.items())
                

