# import requests
# import json
#
# headers = {
#             'authority': 'sou.zhaopin.com',
#             'cache-control': 'max-age=0',
#             'upgrade-insecure-requests': '1',
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
#             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#             'sec-fetch-site': 'same-origin',
#             'sec-fetch-mode': 'navigate',
#             'sec-fetch-user': '?1',
#             'sec-fetch-dest': 'document',
#             'referer': 'https://www.zhaopin.com/',
#             'accept-language': 'zh-CN,zh;q=0.9',
#             'cookie': 'x-zp-client-id=6fda8c91-c692-4072-bb05-ed7821729d7b; sts_deviceid=1740685217a304-0c8ceeab8b02e1-376b4502-1049088-1740685217b380; FSSBBIl1UgzbN7N443S=mN0egr.AUkniHvAZ5nG8WWHQ0Bw0OVyjLVzUbidRS202qIole_qWLwRQ4f92VeI.; _uab_collina=160238182376662700063028; ssxmod_itna=YqUOAKDK7KY5D5P0dD=G7mFG=E23/jC=Qmpx0vcheGzDAxn40iDtoxTZmY=nEliBm+POFAruo48zmRYRx=AC32WTDU4i8DCkro3bDee=D5xGoDPxDeDADYo6DAqiOD7k=DEDmb8DYxGAnKqDgDYQDGuPjD7QDId==So=V0bigWeUPlu4dbqDM7eGXtDnebu0i5=hltOQDzLaDtwtgbM=Px0Pzm8GX9OG5nZmPQBDrzAhPY++zYYx4zYvbSbq3S4AKm756uFD; _jzqx=1.1606138603.1606138603.1.jzqsr=so%2Ecom|jzqct=/link.-; __xsptplus30=30.1.1606138605.1606138605.1%233%7Cwww.so.com%7C%7C%7C%7C%23%23ghY_CLKg-USQDqYLXi9hfovZT_0785Jw%23; adfbid2=0; adfbid=0; sts_sg=1; sts_sid=177d25565451df-0dedf1d13adde9-3e604809-1049088-177d2556546383; sts_chnlsid=121122523; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.K00000K3Zd4fCW_uECt_euLayZfyEhZZ_0teD--NdHlS7wlorI_ehqQrzr9QAdzYo5Ucz4VnVF-SsbBqlEopOW27KwhP6yW6IPTyFmywMduWLny4O2PRxHe924de5GZsLZwc1Srww_QBi6rW1lTwe4G4mbXcUyi2kf-fvhL38EPqXodHxH3owhNfVvET07XPvMIszVnVbxdv-IQ9YG02tki_RNQq.7R_NR2Ar5Od669BCXgjRzeASFDZtwhUVHf632MRRt_Q_DNKnLeMX5DkgboozuPvHWdsHRy2J7jZZOlsfRymoM4EQ9JuIWxDBaurGtIKnLxKfYt_U_DY2yQvTyjtLsqT7jHzlRL5spy59OPt5gKfYtVKnv-WF_tUQQrPMgKfYt_QCJamJj7jQdsRP5Qa1Gk_EdwnmtxyrlAWv3h5USEcSEIe5-g8zxJgOWtMSLqpN2s1f_I-hzEBC.U1Yz0ZDqd_xKJ_L3dIjA8nL30ZKGm1Yk0Zfqd_xKJVUZspoNYnp3dIjA80KGUHYznWR0u1dEuZCk0ZNG5yF9pywd0ZKGujYkn6KWpyfqrHm0UgfqnH0krNtknjDLg1csPH7xn10sn-t1PW0k0AVG5H00TMfqPHfs0AFG5HDdr7tznjwxnWDLg1RsnsKVm1Yknj0kg1D3P1b4njRvPj7xnW0dnNtknjFxn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00mycqn7ts0ANzu1Yz0ZKs5H00UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0A71gv-bm1dsTzdMXh410A-bm1dcHbc0IA7zuvNY5Hm1g1KxnHR10ZwdT1YLrHDdPWRYnW03P164nWnsPHDz0ZF-TgfqnHmkPjDYnHRYnjTsP6K1pyfqmyFWuH7WnHfsnj0sP1FbmsKWTvYqrDF7rDczfYcdfbcLfHFDPfK9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7t1n1mYP1RYg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KGTvP_5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KbmvPb5RDvPj7aPH7anjN7PHnzPjI7wj97wjRdPbmkPjcvwbDdxjfLn1DLPHR1njDsP1bvr0KYTh7buHYLPW0znjc0mhwGujdKnWPKnWD4fWnLwH0zwDfYPDDsnHKjnbfzrHm1wHDknsKEm1Yk0AFY5H00Uv7YI1Ys0AqY5HD0ULFsIjYkc10Wnznzc1cdrjbzn1cYc1cdnj0WnWRsna3snj0snj0Wninzc10WQinsQW0snj0snankQW0snj0sn0K3TLwd5HcLPHTYP1T0TNqv5H08rj-xna3sn7tsQW0sg108nW7xna3zPdtsQWc3g1Dsna3sn7ts0AF1gLKzUvwGujYs0A-1gvPsmHYs0APs5H00mLFW5HmzrHD1%26xst%3Dm1dKPWfkfWRkfW0dwHR1nWfLwRf3wRfdPHuAnHfzPbuKPgsYP1nkP1Rdn10knjT4PW6KmWdKnWPKnWD4fWnLwH0zwDfYPDDsnHKjnbfzrHm1wHDkns715HDzn1T4rjm1nWbLrHD1njcdnWfYg1czPNtk0gTqd_xKJVUZspoNYnp3dIjA807k5IUZspoPSPgfkoWPS07d5HcLPHTYP1TKIjYkPWDYnHfkPHfk0ydk5H0an0cV0yPC5yuWgLKW0Hf4P1T4Pjfkns%26word%3D%26ck%3D8049.4.103.294.400.315.412.187%26shh%3Dwww.baidu.com%26us%3D1.0.1.0.2.1231.0%26wd%3D%26bc%3D110101; urlfrom=121114583; urlfrom2=121114583; adfcid=www.baidu.com; adfcid2=www.baidu.com; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1614141560; acw_tc=2760829316141415631111832e5cf21b6cdc07f017ce204ad4beddf285cf89; locationInfo_search={%22code%22:%22795%22%2C%22name%22:%22%E8%B4%BA%E5%B7%9E%22%2C%22message%22:%22%E5%8C%B9%E9%85%8D%E5%88%B0%E5%B8%82%E7%BA%A7%E7%BC%96%E7%A0%81%22}; 1420ba6bb40c9512e9642a1f8c243891=088674a2-afe5-4b78-9949-9f843e0d7eba; at=2b7d15c058c24c88a9c57897fa4b5b2f; rt=7b0a8d62cd9c4885a778fbcde4617a43; ZP_OLD_FLAG=false; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221087029882%22%2C%22first_id%22%3A%221775dda49e31d8-03523d0cac2fb4-3e604809-1049088-1775dda49e40%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_utm_source%22%3A%22baiduPC%22%2C%22%24latest_utm_medium%22%3A%22CPC%22%2C%22%24latest_utm_campaign%22%3A%22pp%22%2C%22%24latest_utm_content%22%3A%22tj%22%2C%22%24latest_utm_term%22%3A%2228700030%22%7D%2C%22%24device_id%22%3A%221775dda49e31d8-03523d0cac2fb4-3e604809-1049088-1775dda49e40%22%7D; LastCity%5Fid=530; LastCity=%E5%8C%97%E4%BA%AC; ZL_REPORT_GLOBAL={%22/resume/new%22:{%22actionid%22:%22ff4a93eb-2b8a-44f4-808d-9a7692ca3144%22%2C%22funczone%22:%22addrsm_ok_rcm%22}%2C%22//www%22:{%22seid%22:%222b7d15c058c24c88a9c57897fa4b5b2f%22%2C%22actionid%22:%22410790a0-609f-49c8-ab41-b1d3cee856cf-cityPage%22}}; sts_evtseq=12; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1614141629; FSSBBIl1UgzbN7N443T=5FkIJ1sCujhAIVtL0u59V_o8r1BqcyIy2WGLhcR0zIvsaar6vgvlx7SAwPwndo8lAwrosGW1vFrFK.oDRL3P19YipuDr9aDhwfk_5cgAGvl0XGH3063K2ylkpvjTChdOOKTCImh2EvGD82IWtqZJJVQLCQ63VvIB0bIIYf9MijEkXe4NONyNjubdy.ttgQ00RdBroaDiJNHWNwHbzeue_LcLtZ9kJZVAtZlG3dJNDqKYz7S9DNDEJKPiddr49BQAUaTZchKYUysUtbLO58PgCLuMP1IGVEgCfYCj.aHTWGhJQR.q4xqgESlTEwurl.au3onN2F49_cu4jFwPipKacMMhr',
#         }
# url = "https://fe-api.zhaopin.com/c/i/jobs/position-detail-new?at=4c5e59ec8ed140fcb27574fd34e97dfd&rt=d30c1b8f34c048edb59e5684b4ccb35e&number=CC137615180J40075900615&_v=0.41053085&x-zp-page-request-id=51e20a9823aa4fc4bc2b1d347d7aaa59-1614259088304-624518&x-zp-client-id=6fda8c91-c692-4072-bb05-ed7821729d7b&MmEwMD=5to8JcU6u_HpIliN0O_2VjkIrc.rcNMg2Q9Nh1wTzHO1aGmCvLOmxZTpwnRudUFmAJmDsaEsvtmMK4koRgQO10pHp7CaMSz9RS.v7hoZhPbdfIvbTMG5i.nzBZZSYHU8FVk7VnDwMu0K8B1AJbuPRCzc5gpnIf3ZhslNGXYWae1L_cVV7LtND1mewC8ZVXD26Pxw6wA_5CXKe08yPsZve44uADE4CroKO.28_jhItv48qs8oxPouPrqS8AtdhgUnt0uhC21VvaoaVZyU_p4UmMaHj20joq9lHnTDQT0wz8VkEGsmz_AiY_nh5_1qGrwhxjivmXg0zVlK7XCrzRDHjoYglC0Y8oAk1Wjzx5ZlLnHvseZJaiej_xggNTe.pN4hudgGJKMxrTQhqUntOBvp09qao9G3iw11IeEZGjMNyOzsrMg6KA.A756CCU4_cjoE0qvp"
# res = requests.get(url, headers=headers)
#
# print(json.loads(res.text))
import random
user_agent = [
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
            "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
            "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
            "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
            "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
            "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
            "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
            "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
            "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
        ]
# for i in range(10):
#     print(random.randint(1, 10))

headers = {
            'authority': 'sou.zhaopin.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.zhaopin.com/',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'x-zp-client-id=6fda8c91-c692-4072-bb05-ed7821729d7b; sts_deviceid=1740685217a304-0c8ceeab8b02e1-376b4502-1049088-1740685217b380; FSSBBIl1UgzbN7N443S=mN0egr.AUkniHvAZ5nG8WWHQ0Bw0OVyjLVzUbidRS202qIole_qWLwRQ4f92VeI.; _uab_collina=160238182376662700063028; ssxmod_itna=YqUOAKDK7KY5D5P0dD=G7mFG=E23/jC=Qmpx0vcheGzDAxn40iDtoxTZmY=nEliBm+POFAruo48zmRYRx=AC32WTDU4i8DCkro3bDee=D5xGoDPxDeDADYo6DAqiOD7k=DEDmb8DYxGAnKqDgDYQDGuPjD7QDId==So=V0bigWeUPlu4dbqDM7eGXtDnebu0i5=hltOQDzLaDtwtgbM=Px0Pzm8GX9OG5nZmPQBDrzAhPY++zYYx4zYvbSbq3S4AKm756uFD; _jzqx=1.1606138603.1606138603.1.jzqsr=so%2Ecom|jzqct=/link.-; __xsptplus30=30.1.1606138605.1606138605.1%233%7Cwww.so.com%7C%7C%7C%7C%23%23ghY_CLKg-USQDqYLXi9hfovZT_0785Jw%23; adfbid2=0; adfbid=0; sts_sg=1; sts_sid=177d25565451df-0dedf1d13adde9-3e604809-1049088-177d2556546383; sts_chnlsid=121122523; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.K00000K3Zd4fCW_uECt_euLayZfyEhZZ_0teD--NdHlS7wlorI_ehqQrzr9QAdzYo5Ucz4VnVF-SsbBqlEopOW27KwhP6yW6IPTyFmywMduWLny4O2PRxHe924de5GZsLZwc1Srww_QBi6rW1lTwe4G4mbXcUyi2kf-fvhL38EPqXodHxH3owhNfVvET07XPvMIszVnVbxdv-IQ9YG02tki_RNQq.7R_NR2Ar5Od669BCXgjRzeASFDZtwhUVHf632MRRt_Q_DNKnLeMX5DkgboozuPvHWdsHRy2J7jZZOlsfRymoM4EQ9JuIWxDBaurGtIKnLxKfYt_U_DY2yQvTyjtLsqT7jHzlRL5spy59OPt5gKfYtVKnv-WF_tUQQrPMgKfYt_QCJamJj7jQdsRP5Qa1Gk_EdwnmtxyrlAWv3h5USEcSEIe5-g8zxJgOWtMSLqpN2s1f_I-hzEBC.U1Yz0ZDqd_xKJ_L3dIjA8nL30ZKGm1Yk0Zfqd_xKJVUZspoNYnp3dIjA80KGUHYznWR0u1dEuZCk0ZNG5yF9pywd0ZKGujYkn6KWpyfqrHm0UgfqnH0krNtknjDLg1csPH7xn10sn-t1PW0k0AVG5H00TMfqPHfs0AFG5HDdr7tznjwxnWDLg1RsnsKVm1Yknj0kg1D3P1b4njRvPj7xnW0dnNtknjFxn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00mycqn7ts0ANzu1Yz0ZKs5H00UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0A71gv-bm1dsTzdMXh410A-bm1dcHbc0IA7zuvNY5Hm1g1KxnHR10ZwdT1YLrHDdPWRYnW03P164nWnsPHDz0ZF-TgfqnHmkPjDYnHRYnjTsP6K1pyfqmyFWuH7WnHfsnj0sP1FbmsKWTvYqrDF7rDczfYcdfbcLfHFDPfK9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7t1n1mYP1RYg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KGTvP_5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KbmvPb5RDvPj7aPH7anjN7PHnzPjI7wj97wjRdPbmkPjcvwbDdxjfLn1DLPHR1njDsP1bvr0KYTh7buHYLPW0znjc0mhwGujdKnWPKnWD4fWnLwH0zwDfYPDDsnHKjnbfzrHm1wHDknsKEm1Yk0AFY5H00Uv7YI1Ys0AqY5HD0ULFsIjYkc10Wnznzc1cdrjbzn1cYc1cdnj0WnWRsna3snj0snj0Wninzc10WQinsQW0snj0snankQW0snj0sn0K3TLwd5HcLPHTYP1T0TNqv5H08rj-xna3sn7tsQW0sg108nW7xna3zPdtsQWc3g1Dsna3sn7ts0AF1gLKzUvwGujYs0A-1gvPsmHYs0APs5H00mLFW5HmzrHD1%26xst%3Dm1dKPWfkfWRkfW0dwHR1nWfLwRf3wRfdPHuAnHfzPbuKPgsYP1nkP1Rdn10knjT4PW6KmWdKnWPKnWD4fWnLwH0zwDfYPDDsnHKjnbfzrHm1wHDkns715HDzn1T4rjm1nWbLrHD1njcdnWfYg1czPNtk0gTqd_xKJVUZspoNYnp3dIjA807k5IUZspoPSPgfkoWPS07d5HcLPHTYP1TKIjYkPWDYnHfkPHfk0ydk5H0an0cV0yPC5yuWgLKW0Hf4P1T4Pjfkns%26word%3D%26ck%3D8049.4.103.294.400.315.412.187%26shh%3Dwww.baidu.com%26us%3D1.0.1.0.2.1231.0%26wd%3D%26bc%3D110101; urlfrom=121114583; urlfrom2=121114583; adfcid=www.baidu.com; adfcid2=www.baidu.com; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1614141560; acw_tc=2760829316141415631111832e5cf21b6cdc07f017ce204ad4beddf285cf89; locationInfo_search={%22code%22:%22795%22%2C%22name%22:%22%E8%B4%BA%E5%B7%9E%22%2C%22message%22:%22%E5%8C%B9%E9%85%8D%E5%88%B0%E5%B8%82%E7%BA%A7%E7%BC%96%E7%A0%81%22}; 1420ba6bb40c9512e9642a1f8c243891=088674a2-afe5-4b78-9949-9f843e0d7eba; at=2b7d15c058c24c88a9c57897fa4b5b2f; rt=7b0a8d62cd9c4885a778fbcde4617a43; ZP_OLD_FLAG=false; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221087029882%22%2C%22first_id%22%3A%221775dda49e31d8-03523d0cac2fb4-3e604809-1049088-1775dda49e40%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_utm_source%22%3A%22baiduPC%22%2C%22%24latest_utm_medium%22%3A%22CPC%22%2C%22%24latest_utm_campaign%22%3A%22pp%22%2C%22%24latest_utm_content%22%3A%22tj%22%2C%22%24latest_utm_term%22%3A%2228700030%22%7D%2C%22%24device_id%22%3A%221775dda49e31d8-03523d0cac2fb4-3e604809-1049088-1775dda49e40%22%7D; LastCity%5Fid=530; LastCity=%E5%8C%97%E4%BA%AC; ZL_REPORT_GLOBAL={%22/resume/new%22:{%22actionid%22:%22ff4a93eb-2b8a-44f4-808d-9a7692ca3144%22%2C%22funczone%22:%22addrsm_ok_rcm%22}%2C%22//www%22:{%22seid%22:%222b7d15c058c24c88a9c57897fa4b5b2f%22%2C%22actionid%22:%22410790a0-609f-49c8-ab41-b1d3cee856cf-cityPage%22}}; sts_evtseq=12; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1614141629; FSSBBIl1UgzbN7N443T=5FkIJ1sCujhAIVtL0u59V_o8r1BqcyIy2WGLhcR0zIvsaar6vgvlx7SAwPwndo8lAwrosGW1vFrFK.oDRL3P19YipuDr9aDhwfk_5cgAGvl0XGH3063K2ylkpvjTChdOOKTCImh2EvGD82IWtqZJJVQLCQ63VvIB0bIIYf9MijEkXe4NONyNjubdy.ttgQ00RdBroaDiJNHWNwHbzeue_LcLtZ9kJZVAtZlG3dJNDqKYz7S9DNDEJKPiddr49BQAUaTZchKYUysUtbLO58PgCLuMP1IGVEgCfYCj.aHTWGhJQR.q4xqgESlTEwurl.au3onN2F49_cu4jFwPipKacMMhr',
        }
# print(list(headers.values()))


# for i in range(3):
#     value = random.choice(user_agent)
#     headers['user-agent'] = value
#     print(headers)

# "financingStageName": "未融资",
# "companyName": "北京傲盾软件有限责任公司",
# "companyNum ber": "CZ137615180",
# "menVipUrl": "",
# "menVipLevel": 0,
# "industryNameLevel": "IT服务,计算机软件",
# "companySize": "100-299人",
# "companyDescription": "　北京傲盾软件有限公司公司，国家高新技术企业，国内著名网络安全解决方案提供商。公司成立于1998年，现有员工近200人，下辖兰杜互联子公司和南昌分公司。经过10多年的沉淀，现傲盾针对IDC构建了一整套的网络安全和信息安全产品及服务体系。用户遍及各个行业，技术能力和市场占有率均处于业内领先水平。 傲盾优势： 1. 专业性，十多年的技术沉淀，傲盾公司每年投入研发的预算超过年利润的60%。拥有行业高效的研发团队，经验丰富的技术支持团队。 2.整体公司处于高速发展期，2011-2013傲盾实现每年销售收入翻一番。 3.参与国家信息安全系统标准制定，傲盾从2013年开始跟国家相关部委和政策决策部门合作，参与标准制定并提供强有力技术支持。 4.产品市场占有率行业前列。DDOS产品被誉为国内DDOS产品三大厂商，拥有各项国内外安全资质。信息安全管控产品高端用户市场占有率第一 整体市场覆盖第一 5.跟国家相关部委保持紧密联系和合作，为公司提供强有力的战略依据，以实现公司高度、健康、稳定的发展。 6.公司提供业优厚的福利薪酬体系，薪资水平位于业内前列。同时为适应公司高度发展，提供充足的晋升空间。 2014年初，习主席任中央网络安全和信息化小组组长，相信国家对于行业的高度重视，会给安全行业带来更多的发展机遇和挑战，在此我们期待更多精英的加入！ 傲盾典型用户 中央政府：工业和信息化部 国家税务总局 国家质检总局 各省通信管理局.... 电信运营商： 中国电信 中国联通 中国移动 中国铁通 .... 互联网巨头： 阿里巴巴集团 百度 新浪 华数集团 ..... 著名IDC企业：世纪互联 阿里云 蓝汛 鹏博士电信传媒集团 .... ",
# "companyUrl": "http://special.zhaopin.com/pagepublish/13761518/job.html",
# "bestEmployerType": 0,
# "bestEmployerLabel": [],
# "industryLevel": "IT服务,计算机软件",


# "detailedPosition": {
# "welfareLabel": [
# {
# "state": 0,
# "value": "五险一金"
# },
# {
# "state": 0,
# "value": "带薪年假"
# },
# {
# "state": 0,
# "value": "节日福利"
# },
# {
# "state": 0,
# "value": "周末双休"
# }
# ],
# "workType": "全职",
# "tradingArea": "",
# "subJobType": "53",
# "positionStatus": 3,
# "skillLabel": [
# {
# "state": 0,
# "value": "Python"
# },
# {
# "state": 0,
# "value": "NLP"
# },
# {
# "state": 0,
# "value": "机器学习"
# },
# {
# "state": 0,
# "value": "NumPy"
# },
# {
# "state": 0,
# "value": "python爬虫"
# },
# {
# "state": 0,
# "value": "数据采集"
# },
# {
# "state": 0,
# "value": "ElasticSearch"
# }
# ],
# "jobDesc": "<div> 岗位职责：</div><div> 1、采用多种数据获取技术、方式, 对公开网站的统计数据及市场数据的网络抓取，确保数据获取的效率和准确性；</div><div> 2、对抓取数据进行清洗、整理、入库；</div><div> 3、进行数据处理及可视化开发工作；</div><div> 4、解决常见的反爬虫问题；</div><div> 5、负责nlp自然语言算法的实现（比如：自然语言分类算法、自然语言聚类算法、关联算法等）；</div><div> 6、文本分析，机器学习，数据挖掘等工作；</div><div> 7、根据业务需求，研究开发相关算法模型；</div><div> 8、负责相关算法项目的维护、调试、优化和部署等工作；</div><div> 9、参与python框架的设计、维护、优化等工作。</div><div> 任职要求：</div><div> 1、大学本科及以上学历，计算机相关专业，基础扎实;</div><div> 2、精通Python语言的开发，工作经验3年以上，代码风格良好；</div><div> 3、精通常用Python爬虫框架Scrapy、Pyspider中的至少一种;</div><div> 4、精通网页抓取原理及解析技术，熟练使用基于正则表达式、XPath、CSS等网页信息抽取技术;</div><div> 5、精通网络抓包工具，如Fiddler、Wireshark等；</div><div> 6、精通python web框架 Django、Flask、Tornado中的至少一种;</div><div> 7、熟练掌握Mysql、es等数据库；</div><div> 8、掌握python主流数据处理库包，如pandas、numpy、scipy等；</div><div> 9、熟悉深度学习工具Tensorflow/PyTorch/scikit-learn等优先；</div><div> 10. 熟悉逻辑回归、时间序列、决策树、随机森林、XGBoost等建模算法以及各种变量筛选与降维方法，熟练构建各种分类、聚类、预测等模型</div><div> 11、熟练使用matplotlib、seaborn、Pyecharts等工具进行数据可视化</div><div> 12、 工作认真，细心，有条理；积极性高，求知欲强；具有较强的沟通能力及团队合作精神。</div>",
# "workAddress": "南三环西路16号2号楼1706室",
# "latitude": "39.85474",
# "longitude": "116.36821",
# "positionPublishTime": "2021-02-26 00:20:02",
# "education": "本科",
# "positionUrl": "http://jobs.zhaopin.com/CCL1251743210J40107651715.htm",
# "applyType": "1",
# "salary60": "1.6万-1.7万",
# "positionWorkingExp": "1-3年",
# "positionCityId": "530",
# "positionWorkCity": "北京",
# "recruitNumber": 2,
# "salaryCount": "",
# "performanceBonus": "",
# "positionNumber": "CCL1251743210J40107651715",
# "positionName": "python工程师",
# "positionCityDistrict": "",
# "positionCommercialLabel": [],
# "chatWindow": 1,
# "hasAppliedPosition": false,
# "positionHighlight": "五险一金、出差补贴、扁平化管理、发展空间",
# "futureJob": false,
# "futureJobUrl": "",
# "bestEmployerType": 0,
# "bestEmployerLabel": [],
# "companyName": "北京金正数联能源科技有限公司",
# "companyNumber": "CZL1251743210",
# "menVipUrl": "",
# "menVipLevel": 0,
# "jobDescPC": "<div> 岗位职责：</div><div> 1、采用多种数据获取技术、方式, 对公开网站的统计数据及市场数据的网络抓取，确保数据获取的效率和准确性；</div><div> 2、对抓取数据进行清洗、整理、入库；</div><div> 3、进行数据处理及可视化开发工作；</div><div> 4、解决常见的反爬虫问题；</div><div> 5、负责nlp自然语言算法的实现（比如：自然语言分类算法、自然语言聚类算法、关联算法等）；</div><div> 6、文本分析，机器学习，数据挖掘等工作；</div><div> 7、根据业务需求，研究开发相关算法模型；</div><div> 8、负责相关算法项目的维护、调试、优化和部署等工作；</div><div> 9、参与python框架的设计、维护、优化等工作。</div><div> 任职要求：</div><div> 1、大学本科及以上学历，计算机相关专业，基础扎实;</div><div> 2、精通Python语言的开发，工作经验3年以上，代码风格良好；</div><div> 3、精通常用Python爬虫框架Scrapy、Pyspider中的至少一种;</div><div> 4、精通网页抓取原理及解析技术，熟练使用基于正则表达式、XPath、CSS等网页信息抽取技术;</div><div> 5、精通网络抓包工具，如Fiddler、Wireshark等；</div><div> 6、精通python web框架 Django、Flask、Tornado中的至少一种;</div><div> 7、熟练掌握Mysql、es等数据库；</div><div> 8、掌握python主流数据处理库包，如pandas、numpy、scipy等；</div><div> 9、熟悉深度学习工具Tensorflow/PyTorch/scikit-learn等优先；</div><div> 10. 熟悉逻辑回归、时间序列、决策树、随机森林、XGBoost等建模算法以及各种变量筛选与降维方法，熟练构建各种分类、聚类、预测等模型</div><div> 11、熟练使用matplotlib、seaborn、Pyecharts等工具进行数据可视化</div><div> 12、 工作认真，细心，有条理；积极性高，求知欲强；具有较强的沟通能力及团队合作精神。</div>",
# "emplType": "全职",
# "jobStatus": 3,
# "publishTime": "2021-02-26 00:20:02",
# "workingExp": "1-3年",
# "cityId": "530",
# "workCity": "北京",
# "number": "CCL1251743210J40107651715",
# "name": "python工程师",
# "cityDistrict": "",
# "staff": {
# "authenticationState": 1,
# "avatar": "https://rd5-public.zhaopin.cn/imgs/avatar_m2.png",
# "hrJob": "经理",
# "hrOnlineIocState": 0,
# "hrOnlineState": "刚刚活跃",
# "hrResumeOperationState": "处理简历极快",
# "id": 1087728613,
# "modularState": 1,
# "staffName": "张旭",
# "state": 1
# },
# "url": "//www.zhaopin.com/beijing/",
# "emailListPc": "http://jobs.zhaopin.com/CCL1251743210J40107651715.htm"
# },