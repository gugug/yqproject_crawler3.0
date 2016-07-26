# coding=utf-8
from crawl_weibo import *
from combine.text_analyse import *
from get_tpw import *

__author__ = 'gu'
"""
5.28 测试完毕
"""
def cluster():
    """
    get_tpw 提取标题和关键字
    title_cluster 进行标题的聚类
    :return: cluster_dict,聚类后的字典 {bid1:[(title1,blog1,word1),(title1,blog2,word2)], bid2:[(title2,blog4,word4)]}

    """
    cluster_dict = {}

    print "全局的长度,表示猎头数", len(WeiboPage.all_hunterlist)
    for one_dict in WeiboPage.all_hunterlist:
        for (keys, values) in one_dict.items():
            for j in values:
                WeiboPage.detected_tpdict.setdefault(j[1], j[2])  # 我把博文id作为键，博文作为值
    print "字典长度", len(WeiboPage.detected_tpdict)

    bid_list, title_list, tw_list = get_tpw(WeiboPage.detected_tpdict)  # 提取标题和关键字

    index_result = title_cluster(title_list)  # 聚类返回索引

    for com in index_result:
        print "该类的代表bid及标题,及博文关键字", bid_list[com[0]], title_list[com[0]], tw_list[com[0]]
        for bid_index in com:
            bid = bid_list[bid_index]
            print "         ", bid, WeiboPage.detected_tpdict[bid]
            tbw_tuple = (title_list[com[0]], WeiboPage.detected_tpdict[bid], tw_list[bid_index])  # （固定第一个的标题，博文，关键词）
            cluster_dict.setdefault(bid_list[com[0]], []).append(tbw_tuple)

    print "话题聚类完毕"
    return cluster_dict
