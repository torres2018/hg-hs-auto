#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2022/6/10 9:33
# @Author  : Torres
# @Email   : 862578103@qq.com
# @File    : NsData.py
# @Software: PyCharm

# 01.供应商创建测试参数
supplierCreation_data = {
                         "brand":"Eleaf牌/依丽芙牌",
                         "address":"上海普陀区长风公园",
                         "register":"China",
                         "returns":"英国伦敦",
                         "currency":"CNY",
                         "department":"B2B事业部",
                         "subject":"爱奇迹（深圳）技术有限公司",
                         }

# 02.AR申请单数据
applicationForm_data = {"customer":"CU000024813 HG-UI测试专用", "money":1000, "date":"2025-02-16", "explain":"hello"}

# 03.创建采购单测试参数
purchaseCreate_data = {"good1":"PN0000000057161", "number":1000, "good2":"PN0000000057161","date":"2022-06-01"}

# 04.制作采购单副本数据
purchaseCopy_data = {"code":"PO000013491"}

# 05.送货通知单【暂无】

# 06.创建商品数据
productCreation_data = {
                            "brand":"Eleaf牌/依丽芙牌",
                            "norms":"Type",
                            "specs":"Strength",
                            "date":30,
                            "supplier":"VD000002760 深圳市米茄科技有限公司",
                            "unit":"个",
                            }

# 07.创建货品数据
itemCreation_data = {
                            "norms":"0.1 x 0.5mm",# 0.1 x 0.3mm/0.1 x 0.4mm/0.1 x 0.5mm
                            "specs":"10mg/ml",# 10mg/ml,11mg/ml,12mg/ml
                            }

# 08.外部采购价创建测试参数
purchasePrice_data = {"supplier":"VD000002760 深圳市米茄科技有限公司", "price":100}

# 09.库存调整单数据
inventoryAdjustment_data = {
                            "company":"母公司 : Felicita Vita Privat Ltd. : Geek Miracle International Holdings Limited : Geek Miracle (BVI) Limited : IMiracle (HK) Limited",
                            "product":"PN0000000056956",
                            "warehouse":"深圳仓-新香港公司",
                            "quantity":1000
                            }
