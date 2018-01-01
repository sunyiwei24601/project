# -*- coding:utf-8 -*-"""@author:Levy@file:internet_login.py@time:2017/12/1713:07"""
import requests
params={'Username':'1027220030544@tel','Password':'294239'}
r=requests.post("https://wlan.ct10000.com/style/cjdx/index.jsp?paramStr=0UvdVfQabJ9L%2B6K9Ho8gaZdZXsdL9ejlkkCGntI6ExVZ1x%2BhkunX7AYB18fGvQWNfJ4uGScNG6QflW65EcLD9KDKDuk78%2BicfiXfriqHgzD9ABwxyZSUZbrwyKg6%2F2NxZl4RlHVQPjeXVlePoby74Jl3tkmbYXuLIrA4EKrENiSJNN9KHCMbx4Py2KtGGHzHOViVd95eMcM6W%2FfDETS%2FhqzLGAIe8aJpN%2F8MhuFYlrLePPkPK3Ka2fKKDE9cuauKC2HAEp7whlCktr2hsMgAPxQ8qAZlfiTVkC7PDL1Utp4%2FS1I9x%2BzeJ4n%2BXDNsEJJug4Us80PYVxJHTJAdUKezpe4XGPup7k8k")
print(r.text)