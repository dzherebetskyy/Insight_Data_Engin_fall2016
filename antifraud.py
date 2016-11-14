# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:41:49 2016
@author: Danylo Zherebetskyy

"""
#import pandas as pd
import sys

def read_file1(file1):
    """read files and returns list of lists with values"""
    f_data=[]
    f_open=open(file1,'r')
    next(f_open)  # skip the header-line
    for line in f_open:
        vals=line.strip('\n').split(',')
        f_data.append(vals)
    #print int(f_data[1][1])
    #print type(int(f_data[1][1]))
    f_open.close()
    return f_data 

def early_pay(list1):
    """creates a dictionary of all previous transactions as undirected graph"""
    pay={}
    for i in range(len(list1)):
        to1=int(list1[i][1])
        from1=int(list1[i][2])
        if to1 not in pay:
            pay[to1]=list()
        pay[to1].append(from1)
        if from1 not in pay:
            pay[from1]=list()
        pay[from1].append(to1)
    return pay

def feature1(f_data,f_stream):
    """checks if users (from f_stream) did transactions between each other before (in f_data)"""
    out1=open('paymo_output/output1.txt','w+')
    for line in f_stream:
        to1=int(line[1])
        from1=int(line[2])
        #print to1, from1, "feature11"
        if connect1(f_data,to1,from1):
            out1.write('trusted\n')
        else:
            out1.write('unverified\n')
    out1.close()

def connect1(f_data,to1,from1):
    """checks if two users made transactions between each other before in f_data"""
    if to1 in f_data.keys():
        if from1 in f_data[to1]:
            return True
        else:
            return False
    else:
        return False

def feature2(f_data,f_stream):
    """check if users are connected by a friend"""
    out2=open('paymo_output/output2.txt','w+')
    for line in f_stream:
        to1=int(line[1])
        from1=int(line[2])
        #print to1, from1, "feature2"
        if connect2(f_data,to1,from1):
            out2.write('trusted\n')
        else:
            out2.write('unverified\n')
    out2.close()

def connect2(f_data,to2,from2):
    """check for the second-neighbors connection"""
    if to2 in f_data.keys() and from2 in f_data.keys():
        for i in f_data[to2]:
            if i in f_data[from2]:
                return True
            else:
                return False
    else:
        return False
    
def feature3(f_data,f_stream):
    """checks if users are connected by a 4th degree friend network"""
    out3=open('paymo_output/output3.txt','w+')
    for line in f_stream:
        to1=int(line[1])
        from1=int(line[2])
        #print to1, from1, "feature3"
        if connect4(f_data,to1,from1):
            out3.write('trusted\n')
        else:
            out3.write('unverified\n')
    out3.close()

def connect4(f_data,to1,from1):
    """check for the fourth-neighbors connection\n
    create two lists with 2-degree neighbors and check\n
    if these two lists have at least one common element"""
    
    if to1 in f_data.keys() and from1 in f_data.keys():
        list1=[]
        list2=[]
        for i in f_data[to1]:
            for j in f_data[i]:
                list1.extend(f_data[j])  #adds elementsof List2 one-by-one to an existing List1
        for i in f_data[from1]:
            for j in f_data[i]:
                list2.extend(f_data[j]) 
        #print 'list1:',list1
        #print 'list2:',list2
        for i in list1:
            if i in list2:
                return True
                break
            else:
                return False
    else:
        return False


def main():
    if len(sys.argv) != 6:
        print 'usage: path_to_prog.py /path/to/input1 /path/to/input2 /path/to/output1 /path/to/output2 /path/to/output3'
        sys.exit(1)
        
    #use supplied arguments-files
    file_in1 = sys.argv[1]     #'--count'#sys.argv[1]
    file_in2 = sys.argv[2]     
    file_out1 = sys.argv[3] 
    file_out2 = sys.argv[4]
    file_out3 = sys.argv[5]
    
    f_batch=read_file1(file_in1)
    feature_data=early_pay(f_batch)
    f_stream=read_file1(file_in2)

    feature1(feature_data,f_stream)
    feature2(feature_data,f_stream)
    feature3(feature_data,f_stream)
  
  
if __name__ == '__main__':
    main()