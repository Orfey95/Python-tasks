### count_ip(N):
Собрать статистику по айпишникам браузера, в результате указать N самых частых.<br>
N = 7.
```
Count:  4464 IP address:  54.246.139.111
Count:  4219 IP address:  54.77.132.130
Count:  3170 IP address:  196.11.134.77
Count:  2752 IP address:  54.239.166.115
Count:  2572 IP address:  54.239.166.81
Count:  2319 IP address:  54.240.147.77
Count:  2216 IP address:  54.240.147.15
```
### request_frequency(dT):
Найти частоту запросов в интервал времени dT(минут) и ход решения.<br>
dT = 4.
```
Total duration of requests: 950.0 seconds
Total duration of requests: 15.833333333333334 minutes
Time of first request: 09:01:24
Time of last request: 09:17:14
The period you specify is: 4 minutes
The period you specify is: 240 seconds
Period: 09:01:24 - 09:05:24
Number of requests for a specified period of time: 23654
Period: 09:05:24 - 09:09:24
Number of requests for a specified period of time: 25434
Period: 09:09:24 - 09:13:24
Number of requests for a specified period of time: 25693
The remainder: 230.0 seconds
Period: 09:13:24 - 09:17:14
Number of requests for a remainder period of time: 25219
```
### count_user_agent(N):
Найти N самых частых User-Agent.<br>
N = 7.
```
Count:   18469      User Agent: Amazon CloudFront
Count:   9073       User Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36
Count:   7624       User Agent: Jakarta Commons-HttpClient/3.1
Count:   5469       User Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36
Count:   3458       User Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
Count:   3333       User Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36
Count:   2379       User Agent: Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36
```
### error_code_frequency(dT):
Статистика статус кода S(50xошибок) в интервал времени dT(минут).<br>
dT = 5.
```
Total duration of requests: 950.0 seconds
Total duration of requests: 15.833333333333334 minutes
Time of first request: 09:01:24
Time of last request: 09:17:14
The period you specify is: 5 minutes
The period you specify is: 300 seconds
Period: 09:01:24 - 09:06:24
Number of requests for a specified period of time: 29425
Error code:  500  Count:  15
Period: 09:06:24 - 09:11:24
Number of requests for a specified period of time: 32139
Error code:  500  Count:  4
Period: 09:11:24 - 09:16:24
Number of requests for a specified period of time: 33168
Error code:  500  Count:  1
The remainder: 50.0 seconds
Period: 09:16:24 - 09:17:14
Number of requests for a remainder period of time: 5268
```
### count_max_and_min_link(N):
Найти N самых длинных запросов или самых коротких запросов.<br>
N = 7.
```
The list of links with the maximum length:
Length:      1907                      URL:       /merlin-service-search/rest/adverts?accessKey=0bca88be-0aab-461a-809b-58d9d045b976&client=ANDROID_SEARCH&pageNumber=0&recordsPerPage=0&id=8a81b5ab4fb5fcb1014fbcb610ff08b6;8a8183204dbb2667014dbe0474b2137e;8a81b6344fb64c9d014fbb313555534f;8a8183224a5f284a014aad873dd659ce;8a8183874df8b5e6014dfb24616e0b9f;8a81b58f4f463b9a014f4a92ce8d362a;8a81b6a74ebb2ca0014ec1c89c1d390c;8a81b3a44e25d464014e2adffc7435a8;8a8183674dbb3f3c014dc39da5eb578e;8a8184db46f2342c0147108c7a615da5;8a81b58e4f835944014f886b1779537e;8a81b5504edae4dd014ef2697ad3647b;8a81b5094edad57d014ef3ec03237ab7;8a81b58e4f5c70a3014f63eadc265157;8a81b64e4f01bcca014f07ae4ae5396d;8a81836748efe6b101499e0339082b91;8a81833a45a8f919014605917ffd7ec7;8a81b5e94fdb8104014fe1da0e0d5a21;8a81833a4532350301454b9a49cc2f21;8a81b64e4f22c9d6014f2bb6188f6dd2;8a8183fe4b2c6cbc014b44344b7044f2;8a8184ae4dbb3c77014dd2bb6dc5793d;8a8183554dbb2ce1014de083ffea17ab;8a81b6624e4b003d014e76f42c1f1c0e;8aa782603dca00cc013dcb16c9ea2ca3;8a8183234a5f11ea014a77d7fd374db7;8a8183cf4cbe2bbd014ce0c584d1741d;8a8184404dbb3d13014dc81268bf1cf8;8a8183554dbb2ce1014dc848ec3f19c3;8a8184fb47abffea0147c46e3fc042ad;8a81b6e74fad0531014fd293ecd3522f;8a8184e14d72c786014d94fd1fa15934;8a8183da4ffd7b69015009b4f12a144d;8a81b6d34f5c43f5014f5facbcac361a;8a81b64e4f2d90f0014f305a6abc0fdf;8a81b22e4e026dbc014e25f37eb215be;8a8184964d283d7a014d33eed24b0df3;8a81b6344fd0a2d0014fd5a5b64e4b5f;8a8184da4cbe2c31014cc24513cf3340;8a81b3094e02689b014e1d18bccb13c0;8a8184554d28022a014d2d3ed9bc3d17;8a81b6d04f73c42a014f86a471644ce7;8a8183324817f16601484516737f16c4;8a8184db46f2342c0146f5a643bf020c;8a81b5184fb636ba014fbbea7b9676d8;8a8183de4c990f9b014ca1e65d763cbb;8a8184dc4cff4b88014d008b405f1704&advertiserId=&channel=&makeModel=&manufactureYear=&price=&mileageInKm=&engineCapacityInCC=&lat=-26.19489&lon=28.04128&distance=&keywords=&bodyType=&advertiserType=&isUsed=&sortBy=&return=resultType%7Cresults%7CnumFound
Length:      1485                      URL:       /carandcommercialpricerangeszar/under-10-000/carandcommercialpricerangeszar/10-000-to-24-999/carandcommercialpricerangeszar/25-000-to-39-999/carandcommercialpricerangeszar/40-000-to-54-999/carandcommercialpricerangeszar/55-000-to-69-999/carandcommercialpricerangeszar/70-000-to-84-999/carandcommercialpricerangeszar/85-000-to-99-999/carandcommercialpricerangeszar/100-000-to-124-999/carandcommercialpricerangeszar/125-000-to-149-999/carandcommercialpricerangeszar/150-000-to-174-999/radius/200km/bikeandcarmileageranges/below-1-000-km/bikeandcarmileageranges/1-000-km-to-4-999-km/bikeandcarmileageranges/5-000-km-to-9-999-km/bikeandcarmileageranges/10-000-km-to-19-999-km/bikeandcarmileageranges/20-000-km-to-49-999-km/bikeandcarmileageranges/50-000-km-to-74-999-km/bikeandcarmileageranges/75-000-km-to-99-999-km/carenginecapacityranges/1-6l-to-1-8l/carenginecapacityranges/1-9l-to-2-0l/carenginecapacityranges/2-1l-to-2-5l/makemodel/make/alfa-romeo/makemodel/make/audi/model/a3/makemodel/make/lexus/model/is/makemodel/make/bmw/model/1-series/makemodel/make/mazda/model/3/model/mazda3/makemodel/make/facel-vega/model/other/makemodel/make/opel/model/astra/model/corsa/makemodel/make/ford/model/focus/makemodel/make/hyundai/model/i30/makemodel/make/subaru/model/impreza/makemodel/make/volkswagen/model/golf/model/velociti/makemodel/make/kia/model/cerato/model/koup/model/rio/search?sort=MostRecent&county=KwaZulu-Natal&longitude=31.0292&locationName=Durban&latitude=-29.8579&pageNumber=2
Length:      1484                      URL:       /carandcommercialpricerangeszar/under-10-000/carandcommercialpricerangeszar/10-000-to-24-999/carandcommercialpricerangeszar/25-000-to-39-999/carandcommercialpricerangeszar/40-000-to-54-999/carandcommercialpricerangeszar/55-000-to-69-999/carandcommercialpricerangeszar/70-000-to-84-999/carandcommercialpricerangeszar/85-000-to-99-999/carandcommercialpricerangeszar/100-000-to-124-999/carandcommercialpricerangeszar/125-000-to-149-999/carandcommercialpricerangeszar/150-000-to-174-999/radius/200km/bikeandcarmileageranges/below-1-000-km/bikeandcarmileageranges/1-000-km-to-4-999-km/bikeandcarmileageranges/5-000-km-to-9-999-km/bikeandcarmileageranges/10-000-km-to-19-999-km/bikeandcarmileageranges/20-000-km-to-49-999-km/bikeandcarmileageranges/50-000-km-to-74-999-km/bikeandcarmileageranges/75-000-km-to-99-999-km/carenginecapacityranges/1-6l-to-1-8l/carenginecapacityranges/1-9l-to-2-0l/carenginecapacityranges/2-1l-to-2-5l/makemodel/make/alfa-romeo/makemodel/make/audi/model/a3/makemodel/make/lexus/model/is/makemodel/make/bmw/model/1-series/makemodel/make/mazda/model/3/model/mazda3/makemodel/make/facel-vega/model/other/makemodel/make/opel/model/astra/model/corsa/makemodel/make/ford/model/focus/makemodel/make/hyundai/model/i30/makemodel/make/subaru/model/impreza/makemodel/make/volkswagen/model/golf/model/velociti/makemodel/make/kia/model/cerato/model/koup/model/rio/search?sort=MostRecent&gquery=null&locationName=Durban&latitude=-29.8579&longitude=31.0292&county=KwaZulu-Natal
Length:      1482                      URL:       /carandcommercialpricerangeszar/under-10-000/carandcommercialpricerangeszar/10-000-to-24-999/carandcommercialpricerangeszar/25-000-to-39-999/carandcommercialpricerangeszar/40-000-to-54-999/carandcommercialpricerangeszar/55-000-to-69-999/carandcommercialpricerangeszar/70-000-to-84-999/carandcommercialpricerangeszar/85-000-to-99-999/carandcommercialpricerangeszar/100-000-to-124-999/carandcommercialpricerangeszar/125-000-to-149-999/carandcommercialpricerangeszar/150-000-to-174-999/radius/200km/bikeandcarmileageranges/below-1-000-km/bikeandcarmileageranges/1-000-km-to-4-999-km/bikeandcarmileageranges/5-000-km-to-9-999-km/bikeandcarmileageranges/10-000-km-to-19-999-km/bikeandcarmileageranges/20-000-km-to-49-999-km/bikeandcarmileageranges/50-000-km-to-74-999-km/bikeandcarmileageranges/75-000-km-to-99-999-km/carenginecapacityranges/1-6l-to-1-8l/carenginecapacityranges/1-9l-to-2-0l/carenginecapacityranges/2-1l-to-2-5l/makemodel/make/alfa-romeo/makemodel/make/audi/model/a3/makemodel/make/lexus/model/is/makemodel/make/bmw/model/1-series/makemodel/make/mazda/model/3/model/mazda3/makemodel/make/facel-vega/model/other/makemodel/make/opel/model/astra/model/corsa/makemodel/make/ford/model/focus/makemodel/make/hyundai/model/i30/makemodel/make/subaru/model/impreza/makemodel/make/volkswagen/model/golf/model/velociti/makemodel/make/kia/model/cerato/model/koup/model/rio/search?sort=PriceAsc&gquery=null&locationName=Durban&latitude=-29.8579&longitude=31.0292&county=KwaZulu-Natal
Length:      1462                      URL:       /used-cars/kia/cerato/2012-kia-cerato-koup-2-0-sx-kzn-fpa-8a81848f50381e25015038559d89002e/carandcommercialpricerangeszar/under-10-000/carandcommercialpricerangeszar/10-000-to-24-999/carandcommercialpricerangeszar/25-000-to-39-999/carandcommercialpricerangeszar/40-000-to-54-999/carandcommercialpricerangeszar/55-000-to-69-999/carandcommercialpricerangeszar/70-000-to-84-999/carandcommercialpricerangeszar/85-000-to-99-999/carandcommercialpricerangeszar/100-000-to-124-999/carandcommercialpricerangeszar/125-000-to-149-999/carandcommercialpricerangeszar/150-000-to-174-999/radius/200km/bikeandcarmileageranges/below-1-000-km/bikeandcarmileageranges/1-000-km-to-4-999-km/bikeandcarmileageranges/5-000-km-to-9-999-km/bikeandcarmileageranges/10-000-km-to-19-999-km/bikeandcarmileageranges/20-000-km-to-49-999-km/bikeandcarmileageranges/50-000-km-to-74-999-km/bikeandcarmileageranges/75-000-km-to-99-999-km/carenginecapacityranges/1-6l-to-1-8l/carenginecapacityranges/1-9l-to-2-0l/carenginecapacityranges/2-1l-to-2-5l/makemodel/make/alfa-romeo/makemodel/make/audi/model/a3/makemodel/make/lexus/model/is/makemodel/make/bmw/model/1-series/makemodel/make/mazda/model/3/model/mazda3/makemodel/make/facel-vega/model/other/makemodel/make/opel/model/astra/model/corsa/makemodel/make/ford/model/focus/makemodel/make/hyundai/model/i30/makemodel/make/subaru/model/impreza/makemodel/make/volkswagen/model/golf/model/velociti/makemodel/make/kia/model/cerato/model/koup/model/rio
Length:      1456                      URL:       /carandcommercialpricerangeszar/under-10-000/carandcommercialpricerangeszar/10-000-to-24-999/carandcommercialpricerangeszar/25-000-to-39-999/carandcommercialpricerangeszar/40-000-to-54-999/carandcommercialpricerangeszar/55-000-to-69-999/carandcommercialpricerangeszar/70-000-to-84-999/carandcommercialpricerangeszar/85-000-to-99-999/carandcommercialpricerangeszar/100-000-to-124-999/carandcommercialpricerangeszar/125-000-to-149-999/carandcommercialpricerangeszar/150-000-to-174-999/radius/200km/bikeandcarmileageranges/below-1-000-km/bikeandcarmileageranges/1-000-km-to-4-999-km/bikeandcarmileageranges/5-000-km-to-9-999-km/bikeandcarmileageranges/10-000-km-to-19-999-km/bikeandcarmileageranges/20-000-km-to-49-999-km/bikeandcarmileageranges/50-000-km-to-74-999-km/bikeandcarmileageranges/75-000-km-to-99-999-km/carenginecapacityranges/1-6l-to-1-8l/carenginecapacityranges/1-9l-to-2-0l/carenginecapacityranges/2-1l-to-2-5l/makemodel/make/alfa-romeo/makemodel/make/audi/model/a3/makemodel/make/lexus/model/is/makemodel/make/bmw/model/1-series/makemodel/make/mazda/model/3/model/mazda3/makemodel/make/facel-vega/model/other/makemodel/make/opel/model/astra/model/corsa/makemodel/make/ford/model/focus/makemodel/make/hyundai/model/i30/makemodel/make/subaru/model/impreza/makemodel/make/volkswagen/model/golf/model/velociti/makemodel/make/kia/model/cerato/model/koup/model/rio/search?locationName=Durban&latitude=-29.8579&longitude=31.0292&county=KwaZulu-Natal
Length:      1117                      URL:       /bodytype/4x2/bodytype/4x4/bodytype/bakkie/bodytype/suv/bodytype/double-cab/bodytype/single-cab/bodytype/station-wagon/bodytype/kingcab/bodytype/supercab/carandcommercialpricerangeszar/125-000-to-149-999/carandcommercialpricerangeszar/150-000-to-174-999/carandcommercialpricerangeszar/175-000-to-199-999/carandcommercialpricerangeszar/200-000-to-249-999/bikeandcarmileageranges/below-1-000-km/bikeandcarmileageranges/1-000-km-to-4-999-km/bikeandcarmileageranges/5-000-km-to-9-999-km/bikeandcarmileageranges/10-000-km-to-19-999-km/bikeandcarmileageranges/20-000-km-to-49-999-km/bikeandcarmileageranges/50-000-km-to-74-999-km/bikeandcarmileageranges/75-000-km-to-99-999-km/bikeandcarmileageranges/100-000-km-to-149-999-km/caryearrangeszar/2011/caryearrangeszar/2012/caryearrangeszar/2013/caryearrangeszar/2014/caryearrangeszar/2015/makemodel/make/ford/makemodel/make/isuzu/makemodel/make/jeep/makemodel/make/land-rover/makemodel/make/mazda/makemodel/make/mitsubishi/makemodel/make/nissan/makemodel/make/toyota/radius/100km/search?county=KwaZulu-Natal&longitude=31.0292&locationName=Durban&latitude=-29.8579&pageNumber=2
The list of links with the minimum length:
Length:      1                         URL:       /
Length:      5                         URL:       /lite
Length:      5                         URL:       /home
Length:      6                         URL:       /about
Length:      7                         URL:       /mobile
Length:      7                         URL:       /search
Length:      26                        URL:       /merlin-web-za/favicon.ico
```
### count_max_link_to_slash(N, K):
N самых частых запросов до K-го слеша.<br>
N = 4, K = 4.
```
Count:  9231 URL:  /merlin-web-za/web/images
Count:  3498 URL:  /merlin-web-za/bundles/js
Count:  3403 URL:  /merlin-service-search/rest/dblastupdatetime
Count:  3348 URL:  /merlin-web-za/bundles/css
```
### count_upstream():
К-во запросов по апстримам (воркерам).<br>
```
Count:  7166 Upstream:  ajp://10.1.4.69:8009
Count:  7140 Upstream:  ajp://10.1.3.204:8009
Count:  7136 Upstream:  ajp://10.1.4.67:8009
Count:  7136 Upstream:  ajp://10.1.3.205:8009
Count:  7135 Upstream:  ajp://10.1.4.15:8009
Count:  7135 Upstream:  ajp://10.1.3.202:8009
Count:  7135 Upstream:  ajp://10.1.3.203:8009
Count:  7134 Upstream:  ajp://10.1.3.201:8009
Count:  7133 Upstream:  ajp://10.1.4.70:8009
Count:  7133 Upstream:  ajp://10.1.3.88:8009
Count:  7130 Upstream:  ajp://10.1.4.66:8009
Count:  7125 Upstream:  ajp://10.1.4.68:8009
Count:  7114 Upstream:  ajp://10.1.3.86:8009
Count:  6975 Upstream:  ajp://10.1.4.17:8009
```
### count_domain():
По рефереру найти статистику переходов. В результате указать домены и к-во переходов.<br>
```
Count:  51570 Domain:  www.autotrader.co.za
Count:  2010 Domain:  bikes.autotrader.co.za
Count:  1615 Domain:  dealer.autotrader.co.za
Count:  729 Domain:  commercial.autotrader.co.za
Count:  569 Domain:  www.google.co.za
Count:  282 Domain:  leisure.autotrader.co.za
Count:  118 Domain:  www.autofuzion.co.za
Count:  113 Domain:  farm.autotrader.co.za
Count:  89 Domain:  www.google.com
Count:  88 Domain:  www.bing.com
Count:  83 Domain:  autofuzion.co.za
Count:  68 Domain:  plant.autotrader.co.za
Count:  23 Domain:  www.dealer.co.za
Count:  18 Domain:  www2.autotrader.co.za
Count:  11 Domain:  t.co
Count:  7 Domain:  www.google.com.na
Count:  6 Domain:  www.google.co.mz
Count:  5 Domain:  search.yahoo.com
Count:  5 Domain:  www.googleadservices.com
Count:  5 Domain:  www.ananzi.co.za
Count:  5 Domain:  www.google.ae
Count:  5 Domain:  webcache.googleusercontent.com
Count:  4 Domain:  r.search.yahoo.com
Count:  4 Domain:  www.google.co.bw
Count:  3 Domain:  www.search.ask.com
Count:  3 Domain:  www.google.co.zm
Count:  3 Domain:  int.search.tb.ask.com
Count:  2 Domain:  www.google.co.in
Count:  2 Domain:  response.autotrader.co.za
Count:  2 Domain:  www.alfaowner.com
Count:  2 Domain:  www.cayenneworld.com
Count:  2 Domain:  www.google.nl
Count:  2 Domain:  www.google.cm
Count:  2 Domain:  www.google.cd
Count:  2 Domain:  www.google.co.uk
Count:  2 Domain:  www.zapmeta.co.za
Count:  2 Domain:  uk.zapmeta.com
Count:  2 Domain:  www.google.com.my
Count:  2 Domain:  www.google.com.cy
Count:  2 Domain:  www.google.be
Count:  2 Domain:  za.ask.com
Count:  1 Domain:  www.google.com.gh
Count:  1 Domain:  hypnohub.net
Count:  1 Domain:  car.donkiz.co.za
Count:  1 Domain:  156.8.251.153:15871
Count:  1 Domain:  go.mail.ru
Count:  1 Domain:  www.creativelabportal.co.za
Count:  1 Domain:  www.mysearch.com
Count:  1 Domain:  www.google.co.ls
Count:  1 Domain:  www.veemotors.co.za
Count:  1 Domain:  www.google.com.eg
Count:  1 Domain:  tamil.filmibeat.com
Count:  1 Domain:  www.aksons.co.za
Count:  1 Domain:  www.bothadeysel.co.za
Count:  1 Domain:  www.google.co.th
Count:  1 Domain:  www.google.com.ng
Count:  1 Domain:  cayenneworld.com
Count:  1 Domain:  searches.vi-view.com
Count:  1 Domain:  www.google.co.jp
Count:  1 Domain:  goo.gl
```
### upstream_frequency():
К-во запросов по апстримам (воркерам) вdT (30 сек, 1 минуту, 5 мин).<br>
```
Total duration of requests: 950.0 seconds
Total duration of requests: 15.833333333333334 minutes
Time of first request: 09:01:24
Time of last request: 09:17:14
The period you specify is: 0.5 minutes
The period you specify is: 30.0 seconds
Period: 09:01:24 - 09:01:54
Number of requests for a specified period of time: 1272
Count:  106 Upstream:  ajp://10.1.4.17:8009
Count:  86 Upstream:  ajp://10.1.4.67:8009
Count:  88 Upstream:  ajp://10.1.3.201:8009
Count:  90 Upstream:  ajp://10.1.3.204:8009
Count:  82 Upstream:  ajp://10.1.4.68:8009
Count:  110 Upstream:  ajp://10.1.4.15:8009
Count:  89 Upstream:  ajp://10.1.4.70:8009
Count:  109 Upstream:  ajp://10.1.3.202:8009
Count:  86 Upstream:  ajp://10.1.3.203:8009
Count:  87 Upstream:  ajp://10.1.4.69:8009
Count:  86 Upstream:  ajp://10.1.3.205:8009
Count:  87 Upstream:  ajp://10.1.3.88:8009
Count:  83 Upstream:  ajp://10.1.3.86:8009
Count:  81 Upstream:  ajp://10.1.4.66:8009
Period: 09:01:54 - 09:02:24
Number of requests for a specified period of time: 3169
Count:  237 Upstream:  ajp://10.1.4.68:8009
Count:  227 Upstream:  ajp://10.1.4.70:8009
Count:  212 Upstream:  ajp://10.1.4.15:8009
Count:  238 Upstream:  ajp://10.1.3.203:8009
Count:  213 Upstream:  ajp://10.1.3.86:8009
Count:  227 Upstream:  ajp://10.1.3.204:8009
Count:  228 Upstream:  ajp://10.1.3.201:8009
Count:  230 Upstream:  ajp://10.1.4.67:8009
Count:  208 Upstream:  ajp://10.1.3.202:8009
Count:  229 Upstream:  ajp://10.1.3.205:8009
Count:  236 Upstream:  ajp://10.1.4.69:8009
Count:  235 Upstream:  ajp://10.1.4.66:8009
Count:  213 Upstream:  ajp://10.1.4.17:8009
Count:  228 Upstream:  ajp://10.1.3.88:8009
Period: 09:02:24 - 09:02:54
Number of requests for a specified period of time: 3140
Count:  229 Upstream:  ajp://10.1.4.17:8009
Count:  224 Upstream:  ajp://10.1.3.86:8009
Count:  225 Upstream:  ajp://10.1.3.205:8009
Count:  218 Upstream:  ajp://10.1.3.203:8009
Count:  211 Upstream:  ajp://10.1.4.68:8009
Count:  226 Upstream:  ajp://10.1.3.201:8009
Count:  225 Upstream:  ajp://10.1.4.67:8009
Count:  227 Upstream:  ajp://10.1.4.66:8009
Count:  224 Upstream:  ajp://10.1.3.88:8009
Count:  227 Upstream:  ajp://10.1.3.202:8009
Count:  224 Upstream:  ajp://10.1.3.204:8009
Count:  223 Upstream:  ajp://10.1.4.70:8009
Count:  221 Upstream:  ajp://10.1.4.69:8009
Count:  226 Upstream:  ajp://10.1.4.15:8009
Period: 09:02:54 - 09:03:24
Number of requests for a specified period of time: 3270
Count:  245 Upstream:  ajp://10.1.3.201:8009
Count:  231 Upstream:  ajp://10.1.3.203:8009
Count:  229 Upstream:  ajp://10.1.3.202:8009
Count:  235 Upstream:  ajp://10.1.4.70:8009
Count:  241 Upstream:  ajp://10.1.4.15:8009
Count:  232 Upstream:  ajp://10.1.4.68:8009
Count:  233 Upstream:  ajp://10.1.3.205:8009
Count:  232 Upstream:  ajp://10.1.3.86:8009
Count:  233 Upstream:  ajp://10.1.3.204:8009
Count:  233 Upstream:  ajp://10.1.3.88:8009
Count:  232 Upstream:  ajp://10.1.4.67:8009
Count:  224 Upstream:  ajp://10.1.4.66:8009
Count:  228 Upstream:  ajp://10.1.4.69:8009
Count:  228 Upstream:  ajp://10.1.4.17:8009
Period: 09:03:24 - 09:03:54
Number of requests for a specified period of time: 3270
Count:  242 Upstream:  ajp://10.1.3.203:8009
Count:  232 Upstream:  ajp://10.1.4.67:8009
Count:  231 Upstream:  ajp://10.1.3.205:8009
Count:  233 Upstream:  ajp://10.1.4.68:8009
Count:  218 Upstream:  ajp://10.1.3.201:8009
Count:  233 Upstream:  ajp://10.1.3.86:8009
Count:  232 Upstream:  ajp://10.1.4.69:8009
Count:  221 Upstream:  ajp://10.1.4.15:8009
Count:  232 Upstream:  ajp://10.1.3.202:8009
Count:  252 Upstream:  ajp://10.1.4.17:8009
Count:  232 Upstream:  ajp://10.1.3.88:8009
Count:  230 Upstream:  ajp://10.1.4.70:8009
Count:  235 Upstream:  ajp://10.1.4.66:8009
Count:  231 Upstream:  ajp://10.1.3.204:8009
Period: 09:03:54 - 09:04:24
Number of requests for a specified period of time: 3335
Count:  237 Upstream:  ajp://10.1.4.67:8009
Count:  234 Upstream:  ajp://10.1.4.70:8009
Count:  229 Upstream:  ajp://10.1.4.66:8009
Count:  241 Upstream:  ajp://10.1.4.17:8009
Count:  255 Upstream:  ajp://10.1.3.88:8009
Count:  234 Upstream:  ajp://10.1.3.205:8009
Count:  235 Upstream:  ajp://10.1.3.204:8009
Count:  235 Upstream:  ajp://10.1.3.202:8009
Count:  235 Upstream:  ajp://10.1.4.68:8009
Count:  258 Upstream:  ajp://10.1.4.69:8009
Count:  230 Upstream:  ajp://10.1.4.15:8009
Count:  236 Upstream:  ajp://10.1.3.201:8009
Count:  235 Upstream:  ajp://10.1.3.86:8009
Count:  225 Upstream:  ajp://10.1.3.203:8009
Period: 09:04:24 - 09:04:54
Number of requests for a specified period of time: 3218
Count:  234 Upstream:  ajp://10.1.3.205:8009
Count:  238 Upstream:  ajp://10.1.3.86:8009
Count:  232 Upstream:  ajp://10.1.4.15:8009
Count:  233 Upstream:  ajp://10.1.3.202:8009
Count:  234 Upstream:  ajp://10.1.4.70:8009
Count:  232 Upstream:  ajp://10.1.4.68:8009
Count:  234 Upstream:  ajp://10.1.4.66:8009
Count:  203 Upstream:  ajp://10.1.4.17:8009
Count:  235 Upstream:  ajp://10.1.3.204:8009
Count:  230 Upstream:  ajp://10.1.4.67:8009
Count:  233 Upstream:  ajp://10.1.3.203:8009
Count:  212 Upstream:  ajp://10.1.3.88:8009
Count:  231 Upstream:  ajp://10.1.3.201:8009
Count:  222 Upstream:  ajp://10.1.4.69:8009
Period: 09:04:54 - 09:05:24
Number of requests for a specified period of time: 2980
Count:  210 Upstream:  ajp://10.1.4.17:8009
Count:  212 Upstream:  ajp://10.1.3.202:8009
Count:  210 Upstream:  ajp://10.1.3.201:8009
Count:  209 Upstream:  ajp://10.1.4.66:8009
Count:  218 Upstream:  ajp://10.1.4.15:8009
Count:  209 Upstream:  ajp://10.1.3.88:8009
Count:  209 Upstream:  ajp://10.1.4.67:8009
Count:  236 Upstream:  ajp://10.1.4.68:8009
Count:  197 Upstream:  ajp://10.1.4.69:8009
Count:  219 Upstream:  ajp://10.1.3.205:8009
Count:  209 Upstream:  ajp://10.1.3.86:8009
Count:  209 Upstream:  ajp://10.1.3.203:8009
Count:  209 Upstream:  ajp://10.1.3.204:8009
Count:  209 Upstream:  ajp://10.1.4.70:8009
Period: 09:05:24 - 09:05:54
Number of requests for a specified period of time: 2816
Count:  210 Upstream:  ajp://10.1.3.86:8009
Count:  204 Upstream:  ajp://10.1.4.17:8009
Count:  195 Upstream:  ajp://10.1.4.15:8009
Count:  203 Upstream:  ajp://10.1.4.66:8009
Count:  175 Upstream:  ajp://10.1.4.68:8009
Count:  192 Upstream:  ajp://10.1.3.205:8009
Count:  203 Upstream:  ajp://10.1.3.201:8009
Count:  211 Upstream:  ajp://10.1.3.203:8009
Count:  209 Upstream:  ajp://10.1.4.67:8009
Count:  201 Upstream:  ajp://10.1.4.70:8009
Count:  201 Upstream:  ajp://10.1.4.69:8009
Count:  200 Upstream:  ajp://10.1.3.202:8009
Count:  203 Upstream:  ajp://10.1.3.88:8009
Count:  200 Upstream:  ajp://10.1.3.204:8009
Period: 09:05:54 - 09:06:24
Number of requests for a specified period of time: 2955
Count:  210 Upstream:  ajp://10.1.3.202:8009
Count:  219 Upstream:  ajp://10.1.4.15:8009
Count:  197 Upstream:  ajp://10.1.3.86:8009
Count:  207 Upstream:  ajp://10.1.4.17:8009
Count:  202 Upstream:  ajp://10.1.3.203:8009
Count:  210 Upstream:  ajp://10.1.4.66:8009
Count:  213 Upstream:  ajp://10.1.4.69:8009
Count:  218 Upstream:  ajp://10.1.3.204:8009
Count:  211 Upstream:  ajp://10.1.3.205:8009
Count:  210 Upstream:  ajp://10.1.4.68:8009
Count:  212 Upstream:  ajp://10.1.4.70:8009
Count:  209 Upstream:  ajp://10.1.3.88:8009
Count:  210 Upstream:  ajp://10.1.3.201:8009
Count:  214 Upstream:  ajp://10.1.4.67:8009
Period: 09:06:24 - 09:06:54
Number of requests for a specified period of time: 3005
Count:  213 Upstream:  ajp://10.1.3.88:8009
Count:  203 Upstream:  ajp://10.1.4.67:8009
Count:  215 Upstream:  ajp://10.1.4.66:8009
Count:  213 Upstream:  ajp://10.1.3.203:8009
Count:  211 Upstream:  ajp://10.1.3.86:8009
Count:  220 Upstream:  ajp://10.1.3.202:8009
Count:  218 Upstream:  ajp://10.1.4.17:8009
Count:  213 Upstream:  ajp://10.1.3.201:8009
Count:  217 Upstream:  ajp://10.1.4.68:8009
Count:  212 Upstream:  ajp://10.1.3.205:8009
Count:  215 Upstream:  ajp://10.1.4.70:8009
Count:  211 Upstream:  ajp://10.1.4.69:8009
Count:  206 Upstream:  ajp://10.1.4.15:8009
Count:  229 Upstream:  ajp://10.1.3.204:8009
Period: 09:06:54 - 09:07:24
Number of requests for a specified period of time: 3273
Count:  236 Upstream:  ajp://10.1.3.205:8009
Count:  235 Upstream:  ajp://10.1.4.70:8009
Count:  235 Upstream:  ajp://10.1.3.88:8009
Count:  240 Upstream:  ajp://10.1.4.66:8009
Count:  237 Upstream:  ajp://10.1.3.201:8009
Count:  234 Upstream:  ajp://10.1.3.86:8009
Count:  227 Upstream:  ajp://10.1.3.202:8009
Count:  234 Upstream:  ajp://10.1.4.69:8009
Count:  234 Upstream:  ajp://10.1.4.15:8009
Count:  233 Upstream:  ajp://10.1.4.68:8009
Count:  239 Upstream:  ajp://10.1.4.67:8009
Count:  235 Upstream:  ajp://10.1.3.203:8009
Count:  214 Upstream:  ajp://10.1.3.204:8009
Count:  230 Upstream:  ajp://10.1.4.17:8009
Period: 09:07:24 - 09:07:54
Number of requests for a specified period of time: 3063
Count:  215 Upstream:  ajp://10.1.4.67:8009
Count:  211 Upstream:  ajp://10.1.4.66:8009
Count:  220 Upstream:  ajp://10.1.3.88:8009
Count:  222 Upstream:  ajp://10.1.3.202:8009
Count:  217 Upstream:  ajp://10.1.4.15:8009
Count:  227 Upstream:  ajp://10.1.4.17:8009
Count:  218 Upstream:  ajp://10.1.4.69:8009
Count:  214 Upstream:  ajp://10.1.4.68:8009
Count:  220 Upstream:  ajp://10.1.3.205:8009
Count:  221 Upstream:  ajp://10.1.3.86:8009
Count:  218 Upstream:  ajp://10.1.3.203:8009
Count:  217 Upstream:  ajp://10.1.4.70:8009
Count:  216 Upstream:  ajp://10.1.3.204:8009
Count:  215 Upstream:  ajp://10.1.3.201:8009
Period: 09:07:54 - 09:08:24
Number of requests for a specified period of time: 3338
Count:  232 Upstream:  ajp://10.1.4.70:8009
Count:  241 Upstream:  ajp://10.1.3.86:8009
Count:  236 Upstream:  ajp://10.1.4.68:8009
Count:  236 Upstream:  ajp://10.1.3.88:8009
Count:  232 Upstream:  ajp://10.1.3.202:8009
Count:  238 Upstream:  ajp://10.1.4.15:8009
Count:  236 Upstream:  ajp://10.1.4.66:8009
Count:  247 Upstream:  ajp://10.1.4.69:8009
Count:  247 Upstream:  ajp://10.1.3.203:8009
Count:  245 Upstream:  ajp://10.1.3.201:8009
Count:  236 Upstream:  ajp://10.1.3.204:8009
Count:  243 Upstream:  ajp://10.1.4.67:8009
Count:  233 Upstream:  ajp://10.1.3.205:8009
Count:  229 Upstream:  ajp://10.1.4.17:8009
Period: 09:08:24 - 09:08:54
Number of requests for a specified period of time: 3658
Count:  261 Upstream:  ajp://10.1.4.68:8009
Count:  266 Upstream:  ajp://10.1.3.204:8009
Count:  263 Upstream:  ajp://10.1.4.66:8009
Count:  262 Upstream:  ajp://10.1.4.70:8009
Count:  264 Upstream:  ajp://10.1.3.205:8009
Count:  263 Upstream:  ajp://10.1.3.88:8009
Count:  259 Upstream:  ajp://10.1.4.15:8009
Count:  262 Upstream:  ajp://10.1.3.202:8009
Count:  276 Upstream:  ajp://10.1.3.86:8009
Count:  250 Upstream:  ajp://10.1.4.69:8009
Count:  259 Upstream:  ajp://10.1.4.17:8009
Count:  259 Upstream:  ajp://10.1.4.67:8009
Count:  251 Upstream:  ajp://10.1.3.203:8009
Count:  252 Upstream:  ajp://10.1.3.201:8009
Period: 09:08:54 - 09:09:24
Number of requests for a specified period of time: 3326
Count:  235 Upstream:  ajp://10.1.4.17:8009
Count:  229 Upstream:  ajp://10.1.3.204:8009
Count:  238 Upstream:  ajp://10.1.3.86:8009
Count:  237 Upstream:  ajp://10.1.4.68:8009
Count:  236 Upstream:  ajp://10.1.3.201:8009
Count:  229 Upstream:  ajp://10.1.4.67:8009
Count:  235 Upstream:  ajp://10.1.4.69:8009
Count:  235 Upstream:  ajp://10.1.4.15:8009
Count:  244 Upstream:  ajp://10.1.4.70:8009
Count:  250 Upstream:  ajp://10.1.3.202:8009
Count:  232 Upstream:  ajp://10.1.4.66:8009
Count:  240 Upstream:  ajp://10.1.3.88:8009
Count:  243 Upstream:  ajp://10.1.3.203:8009
Count:  234 Upstream:  ajp://10.1.3.205:8009
Period: 09:09:24 - 09:09:54
Number of requests for a specified period of time: 3091
Count:  212 Upstream:  ajp://10.1.3.203:8009
Count:  221 Upstream:  ajp://10.1.3.86:8009
Count:  223 Upstream:  ajp://10.1.3.204:8009
Count:  221 Upstream:  ajp://10.1.3.205:8009
Count:  221 Upstream:  ajp://10.1.3.201:8009
Count:  222 Upstream:  ajp://10.1.4.17:8009
Count:  221 Upstream:  ajp://10.1.4.15:8009
Count:  210 Upstream:  ajp://10.1.4.70:8009
Count:  245 Upstream:  ajp://10.1.3.88:8009
Count:  224 Upstream:  ajp://10.1.4.69:8009
Count:  225 Upstream:  ajp://10.1.4.67:8009
Count:  217 Upstream:  ajp://10.1.4.66:8009
Count:  219 Upstream:  ajp://10.1.4.68:8009
Count:  206 Upstream:  ajp://10.1.3.202:8009
Period: 09:09:54 - 09:10:24
Number of requests for a specified period of time: 3297
Count:  215 Upstream:  ajp://10.1.3.86:8009
Count:  207 Upstream:  ajp://10.1.3.88:8009
Count:  238 Upstream:  ajp://10.1.4.15:8009
Count:  243 Upstream:  ajp://10.1.4.70:8009
Count:  248 Upstream:  ajp://10.1.4.66:8009
Count:  235 Upstream:  ajp://10.1.4.67:8009
Count:  237 Upstream:  ajp://10.1.3.202:8009
Count:  241 Upstream:  ajp://10.1.4.17:8009
Count:  239 Upstream:  ajp://10.1.3.201:8009
Count:  238 Upstream:  ajp://10.1.3.205:8009
Count:  239 Upstream:  ajp://10.1.4.68:8009
Count:  239 Upstream:  ajp://10.1.3.203:8009
Count:  237 Upstream:  ajp://10.1.3.204:8009
Count:  235 Upstream:  ajp://10.1.4.69:8009
Period: 09:10:24 - 09:10:54
Number of requests for a specified period of time: 3063
Count:  216 Upstream:  ajp://10.1.4.69:8009
Count:  216 Upstream:  ajp://10.1.3.204:8009
Count:  233 Upstream:  ajp://10.1.4.67:8009
Count:  225 Upstream:  ajp://10.1.3.202:8009
Count:  218 Upstream:  ajp://10.1.3.88:8009
Count:  227 Upstream:  ajp://10.1.4.17:8009
Count:  223 Upstream:  ajp://10.1.3.205:8009
Count:  214 Upstream:  ajp://10.1.3.201:8009
Count:  214 Upstream:  ajp://10.1.4.68:8009
Count:  216 Upstream:  ajp://10.1.3.86:8009
Count:  217 Upstream:  ajp://10.1.4.15:8009
Count:  210 Upstream:  ajp://10.1.4.66:8009
Count:  218 Upstream:  ajp://10.1.3.203:8009
Count:  211 Upstream:  ajp://10.1.4.70:8009
Period: 09:10:54 - 09:11:24
Number of requests for a specified period of time: 3025
Count:  212 Upstream:  ajp://10.1.3.205:8009
Count:  219 Upstream:  ajp://10.1.4.66:8009
Count:  219 Upstream:  ajp://10.1.4.70:8009
Count:  218 Upstream:  ajp://10.1.3.201:8009
Count:  207 Upstream:  ajp://10.1.4.17:8009
Count:  218 Upstream:  ajp://10.1.3.86:8009
Count:  215 Upstream:  ajp://10.1.3.203:8009
Count:  217 Upstream:  ajp://10.1.3.204:8009
Count:  217 Upstream:  ajp://10.1.4.69:8009
Count:  211 Upstream:  ajp://10.1.4.67:8009
Count:  227 Upstream:  ajp://10.1.4.68:8009
Count:  216 Upstream:  ajp://10.1.3.88:8009
Count:  209 Upstream:  ajp://10.1.3.202:8009
Count:  216 Upstream:  ajp://10.1.4.15:8009
Period: 09:11:24 - 09:11:54
Number of requests for a specified period of time: 3136
Count:  223 Upstream:  ajp://10.1.3.204:8009
Count:  215 Upstream:  ajp://10.1.4.67:8009
Count:  223 Upstream:  ajp://10.1.3.88:8009
Count:  225 Upstream:  ajp://10.1.4.69:8009
Count:  224 Upstream:  ajp://10.1.4.66:8009
Count:  223 Upstream:  ajp://10.1.3.86:8009
Count:  222 Upstream:  ajp://10.1.3.202:8009
Count:  223 Upstream:  ajp://10.1.3.201:8009
Count:  222 Upstream:  ajp://10.1.4.15:8009
Count:  225 Upstream:  ajp://10.1.4.70:8009
Count:  221 Upstream:  ajp://10.1.3.203:8009
Count:  248 Upstream:  ajp://10.1.3.205:8009
Count:  213 Upstream:  ajp://10.1.4.68:8009
Count:  220 Upstream:  ajp://10.1.4.17:8009
Period: 09:11:54 - 09:12:24
Number of requests for a specified period of time: 3344
Count:  242 Upstream:  ajp://10.1.3.202:8009
Count:  256 Upstream:  ajp://10.1.3.88:8009
Count:  241 Upstream:  ajp://10.1.3.203:8009
Count:  239 Upstream:  ajp://10.1.3.201:8009
Count:  239 Upstream:  ajp://10.1.3.204:8009
Count:  237 Upstream:  ajp://10.1.4.67:8009
Count:  245 Upstream:  ajp://10.1.4.15:8009
Count:  239 Upstream:  ajp://10.1.4.68:8009
Count:  212 Upstream:  ajp://10.1.3.205:8009
Count:  235 Upstream:  ajp://10.1.4.66:8009
Count:  239 Upstream:  ajp://10.1.4.17:8009
Count:  240 Upstream:  ajp://10.1.4.69:8009
Count:  237 Upstream:  ajp://10.1.3.86:8009
Count:  239 Upstream:  ajp://10.1.4.70:8009
Period: 09:12:24 - 09:12:54
Number of requests for a specified period of time: 3307
Count:  230 Upstream:  ajp://10.1.4.69:8009
Count:  236 Upstream:  ajp://10.1.4.68:8009
Count:  235 Upstream:  ajp://10.1.3.86:8009
Count:  237 Upstream:  ajp://10.1.4.66:8009
Count:  236 Upstream:  ajp://10.1.3.201:8009
Count:  234 Upstream:  ajp://10.1.3.204:8009
Count:  234 Upstream:  ajp://10.1.3.202:8009
Count:  231 Upstream:  ajp://10.1.4.70:8009
Count:  228 Upstream:  ajp://10.1.4.15:8009
Count:  253 Upstream:  ajp://10.1.3.205:8009
Count:  240 Upstream:  ajp://10.1.4.67:8009
Count:  232 Upstream:  ajp://10.1.3.203:8009
Count:  236 Upstream:  ajp://10.1.3.88:8009
Count:  238 Upstream:  ajp://10.1.4.17:8009
Period: 09:12:54 - 09:13:24
Number of requests for a specified period of time: 3430
Count:  226 Upstream:  ajp://10.1.3.88:8009
Count:  227 Upstream:  ajp://10.1.3.205:8009
Count:  239 Upstream:  ajp://10.1.3.202:8009
Count:  245 Upstream:  ajp://10.1.4.69:8009
Count:  244 Upstream:  ajp://10.1.4.70:8009
Count:  237 Upstream:  ajp://10.1.4.67:8009
Count:  257 Upstream:  ajp://10.1.4.17:8009
Count:  245 Upstream:  ajp://10.1.4.66:8009
Count:  243 Upstream:  ajp://10.1.3.86:8009
Count:  244 Upstream:  ajp://10.1.3.204:8009
Count:  241 Upstream:  ajp://10.1.3.201:8009
Count:  254 Upstream:  ajp://10.1.4.15:8009
Count:  266 Upstream:  ajp://10.1.4.68:8009
Count:  255 Upstream:  ajp://10.1.3.203:8009
Period: 09:13:24 - 09:13:54
Number of requests for a specified period of time: 3370
Count:  244 Upstream:  ajp://10.1.3.202:8009
Count:  231 Upstream:  ajp://10.1.4.17:8009
Count:  244 Upstream:  ajp://10.1.4.67:8009
Count:  242 Upstream:  ajp://10.1.3.201:8009
Count:  245 Upstream:  ajp://10.1.3.86:8009
Count:  250 Upstream:  ajp://10.1.4.70:8009
Count:  231 Upstream:  ajp://10.1.3.203:8009
Count:  242 Upstream:  ajp://10.1.3.204:8009
Count:  232 Upstream:  ajp://10.1.4.15:8009
Count:  219 Upstream:  ajp://10.1.4.68:8009
Count:  242 Upstream:  ajp://10.1.4.69:8009
Count:  256 Upstream:  ajp://10.1.3.88:8009
Count:  241 Upstream:  ajp://10.1.4.66:8009
Count:  242 Upstream:  ajp://10.1.3.205:8009
Period: 09:13:54 - 09:14:24
Number of requests for a specified period of time: 3443
Count:  258 Upstream:  ajp://10.1.3.201:8009
Count:  256 Upstream:  ajp://10.1.3.205:8009
Count:  259 Upstream:  ajp://10.1.3.204:8009
Count:  267 Upstream:  ajp://10.1.3.202:8009
Count:  94 Upstream:  ajp://10.1.4.17:8009
Count:  258 Upstream:  ajp://10.1.4.15:8009
Count:  243 Upstream:  ajp://10.1.3.88:8009
Count:  258 Upstream:  ajp://10.1.3.203:8009
Count:  262 Upstream:  ajp://10.1.4.67:8009
Count:  258 Upstream:  ajp://10.1.4.66:8009
Count:  259 Upstream:  ajp://10.1.4.68:8009
Count:  249 Upstream:  ajp://10.1.4.70:8009
Count:  257 Upstream:  ajp://10.1.3.86:8009
Count:  255 Upstream:  ajp://10.1.4.69:8009
Period: 09:14:24 - 09:14:54
Number of requests for a specified period of time: 3380
Count:  239 Upstream:  ajp://10.1.4.66:8009
Count:  251 Upstream:  ajp://10.1.4.68:8009
Count:  239 Upstream:  ajp://10.1.3.204:8009
Count:  259 Upstream:  ajp://10.1.4.69:8009
Count:  230 Upstream:  ajp://10.1.3.202:8009
Count:  234 Upstream:  ajp://10.1.4.67:8009
Count:  239 Upstream:  ajp://10.1.3.88:8009
Count:  241 Upstream:  ajp://10.1.3.201:8009
Count:  240 Upstream:  ajp://10.1.4.70:8009
Count:  238 Upstream:  ajp://10.1.3.203:8009
Count:  239 Upstream:  ajp://10.1.3.205:8009
Count:  239 Upstream:  ajp://10.1.4.15:8009
Count:  238 Upstream:  ajp://10.1.3.86:8009
Count:  244 Upstream:  ajp://10.1.4.17:8009
Period: 09:14:54 - 09:15:24
Number of requests for a specified period of time: 3249
Count:  216 Upstream:  ajp://10.1.4.69:8009
Count:  234 Upstream:  ajp://10.1.3.204:8009
Count:  235 Upstream:  ajp://10.1.3.203:8009
Count:  217 Upstream:  ajp://10.1.4.17:8009
Count:  232 Upstream:  ajp://10.1.3.86:8009
Count:  235 Upstream:  ajp://10.1.3.202:8009
Count:  236 Upstream:  ajp://10.1.4.66:8009
Count:  233 Upstream:  ajp://10.1.3.205:8009
Count:  235 Upstream:  ajp://10.1.4.15:8009
Count:  221 Upstream:  ajp://10.1.4.68:8009
Count:  237 Upstream:  ajp://10.1.4.67:8009
Count:  234 Upstream:  ajp://10.1.3.88:8009
Count:  237 Upstream:  ajp://10.1.4.70:8009
Count:  232 Upstream:  ajp://10.1.3.201:8009
Period: 09:15:24 - 09:15:54
Number of requests for a specified period of time: 3244
Count:  230 Upstream:  ajp://10.1.3.201:8009
Count:  236 Upstream:  ajp://10.1.3.86:8009
Count:  231 Upstream:  ajp://10.1.3.205:8009
Count:  229 Upstream:  ajp://10.1.4.68:8009
Count:  230 Upstream:  ajp://10.1.4.17:8009
Count:  230 Upstream:  ajp://10.1.3.202:8009
Count:  229 Upstream:  ajp://10.1.4.66:8009
Count:  230 Upstream:  ajp://10.1.3.204:8009
Count:  229 Upstream:  ajp://10.1.3.203:8009
Count:  228 Upstream:  ajp://10.1.4.69:8009
Count:  236 Upstream:  ajp://10.1.3.88:8009
Count:  230 Upstream:  ajp://10.1.4.15:8009
Count:  239 Upstream:  ajp://10.1.4.67:8009
Count:  226 Upstream:  ajp://10.1.4.70:8009
Period: 09:15:54 - 09:16:24
Number of requests for a specified period of time: 3265
Count:  239 Upstream:  ajp://10.1.4.68:8009
Count:  234 Upstream:  ajp://10.1.4.69:8009
Count:  223 Upstream:  ajp://10.1.4.67:8009
Count:  234 Upstream:  ajp://10.1.3.203:8009
Count:  235 Upstream:  ajp://10.1.3.202:8009
Count:  231 Upstream:  ajp://10.1.3.205:8009
Count:  234 Upstream:  ajp://10.1.3.201:8009
Count:  229 Upstream:  ajp://10.1.3.86:8009
Count:  234 Upstream:  ajp://10.1.3.204:8009
Count:  234 Upstream:  ajp://10.1.4.66:8009
Count:  233 Upstream:  ajp://10.1.4.70:8009
Count:  231 Upstream:  ajp://10.1.3.88:8009
Count:  232 Upstream:  ajp://10.1.4.15:8009
Count:  232 Upstream:  ajp://10.1.4.17:8009
Period: 09:16:24 - 09:16:54
Number of requests for a specified period of time: 3248
Count:  235 Upstream:  ajp://10.1.4.17:8009
Count:  235 Upstream:  ajp://10.1.3.86:8009
Count:  229 Upstream:  ajp://10.1.3.201:8009
Count:  230 Upstream:  ajp://10.1.3.202:8009
Count:  228 Upstream:  ajp://10.1.3.88:8009
Count:  232 Upstream:  ajp://10.1.4.67:8009
Count:  232 Upstream:  ajp://10.1.4.70:8009
Count:  232 Upstream:  ajp://10.1.3.205:8009
Count:  230 Upstream:  ajp://10.1.3.204:8009
Count:  231 Upstream:  ajp://10.1.3.203:8009
Count:  231 Upstream:  ajp://10.1.4.15:8009
Count:  230 Upstream:  ajp://10.1.4.66:8009
Count:  231 Upstream:  ajp://10.1.4.68:8009
Count:  230 Upstream:  ajp://10.1.4.69:8009
The remainder: 20.0 seconds
Period: 09:16:54 - 09:17:14
Number of requests for a remainder period of time: 2020
Count:  139 Upstream:  ajp://10.1.3.86:8009
Count:  174 Upstream:  ajp://10.1.4.69:8009
Count:  142 Upstream:  ajp://10.1.4.15:8009
Count:  142 Upstream:  ajp://10.1.4.70:8009
Count:  141 Upstream:  ajp://10.1.4.66:8009
Count:  141 Upstream:  ajp://10.1.3.202:8009
Count:  142 Upstream:  ajp://10.1.3.203:8009
Count:  140 Upstream:  ajp://10.1.3.88:8009
Count:  142 Upstream:  ajp://10.1.3.201:8009
Count:  142 Upstream:  ajp://10.1.3.205:8009
Count:  146 Upstream:  ajp://10.1.3.204:8009
Count:  139 Upstream:  ajp://10.1.4.67:8009
Count:  136 Upstream:  ajp://10.1.4.68:8009
Count:  148 Upstream:  ajp://10.1.4.17:8009
The period you specify is: 1.0 minutes
The period you specify is: 60 seconds
Period: 09:01:24 - 09:02:24
Number of requests for a specified period of time: 4441
Count:  319 Upstream:  ajp://10.1.4.17:8009
Count:  316 Upstream:  ajp://10.1.4.67:8009
Count:  316 Upstream:  ajp://10.1.3.201:8009
Count:  317 Upstream:  ajp://10.1.3.204:8009
Count:  319 Upstream:  ajp://10.1.4.68:8009
Count:  322 Upstream:  ajp://10.1.4.15:8009
Count:  316 Upstream:  ajp://10.1.4.70:8009
Count:  317 Upstream:  ajp://10.1.3.202:8009
Count:  324 Upstream:  ajp://10.1.3.203:8009
Count:  324 Upstream:  ajp://10.1.4.69:8009
Count:  315 Upstream:  ajp://10.1.3.205:8009
Count:  315 Upstream:  ajp://10.1.3.88:8009
Count:  296 Upstream:  ajp://10.1.3.86:8009
Count:  316 Upstream:  ajp://10.1.4.66:8009
Period: 09:02:24 - 09:03:24
Number of requests for a specified period of time: 6410
Count:  457 Upstream:  ajp://10.1.4.17:8009
Count:  456 Upstream:  ajp://10.1.3.86:8009
Count:  459 Upstream:  ajp://10.1.3.205:8009
Count:  449 Upstream:  ajp://10.1.3.203:8009
Count:  443 Upstream:  ajp://10.1.4.68:8009
Count:  471 Upstream:  ajp://10.1.3.201:8009
Count:  457 Upstream:  ajp://10.1.4.67:8009
Count:  451 Upstream:  ajp://10.1.4.66:8009
Count:  457 Upstream:  ajp://10.1.3.88:8009
Count:  456 Upstream:  ajp://10.1.3.202:8009
Count:  457 Upstream:  ajp://10.1.3.204:8009
Count:  458 Upstream:  ajp://10.1.4.70:8009
Count:  449 Upstream:  ajp://10.1.4.69:8009
Count:  467 Upstream:  ajp://10.1.4.15:8009
Period: 09:03:24 - 09:04:24
Number of requests for a specified period of time: 6605
Count:  467 Upstream:  ajp://10.1.3.203:8009
Count:  469 Upstream:  ajp://10.1.4.67:8009
Count:  465 Upstream:  ajp://10.1.3.205:8009
Count:  468 Upstream:  ajp://10.1.4.68:8009
Count:  454 Upstream:  ajp://10.1.3.201:8009
Count:  468 Upstream:  ajp://10.1.3.86:8009
Count:  490 Upstream:  ajp://10.1.4.69:8009
Count:  451 Upstream:  ajp://10.1.4.15:8009
Count:  467 Upstream:  ajp://10.1.3.202:8009
Count:  493 Upstream:  ajp://10.1.4.17:8009
Count:  487 Upstream:  ajp://10.1.3.88:8009
Count:  464 Upstream:  ajp://10.1.4.70:8009
Count:  465 Upstream:  ajp://10.1.4.66:8009
Count:  466 Upstream:  ajp://10.1.3.204:8009
Period: 09:04:24 - 09:05:24
Number of requests for a specified period of time: 6198
Count:  453 Upstream:  ajp://10.1.3.205:8009
Count:  447 Upstream:  ajp://10.1.3.86:8009
Count:  450 Upstream:  ajp://10.1.4.15:8009
Count:  445 Upstream:  ajp://10.1.3.202:8009
Count:  443 Upstream:  ajp://10.1.4.70:8009
Count:  468 Upstream:  ajp://10.1.4.68:8009
Count:  443 Upstream:  ajp://10.1.4.66:8009
Count:  414 Upstream:  ajp://10.1.4.17:8009
Count:  444 Upstream:  ajp://10.1.3.204:8009
Count:  439 Upstream:  ajp://10.1.4.67:8009
Count:  442 Upstream:  ajp://10.1.3.203:8009
Count:  421 Upstream:  ajp://10.1.3.88:8009
Count:  441 Upstream:  ajp://10.1.3.201:8009
Count:  419 Upstream:  ajp://10.1.4.69:8009
Period: 09:05:24 - 09:06:24
Number of requests for a specified period of time: 5771
Count:  407 Upstream:  ajp://10.1.3.86:8009
Count:  411 Upstream:  ajp://10.1.4.17:8009
Count:  414 Upstream:  ajp://10.1.4.15:8009
Count:  413 Upstream:  ajp://10.1.4.66:8009
Count:  385 Upstream:  ajp://10.1.4.68:8009
Count:  403 Upstream:  ajp://10.1.3.205:8009
Count:  413 Upstream:  ajp://10.1.3.201:8009
Count:  413 Upstream:  ajp://10.1.3.203:8009
Count:  423 Upstream:  ajp://10.1.4.67:8009
Count:  414 Upstream:  ajp://10.1.4.70:8009
Count:  414 Upstream:  ajp://10.1.4.69:8009
Count:  410 Upstream:  ajp://10.1.3.202:8009
Count:  412 Upstream:  ajp://10.1.3.88:8009
Count:  418 Upstream:  ajp://10.1.3.204:8009
Period: 09:06:24 - 09:07:24
Number of requests for a specified period of time: 6278
Count:  448 Upstream:  ajp://10.1.3.88:8009
Count:  442 Upstream:  ajp://10.1.4.67:8009
Count:  455 Upstream:  ajp://10.1.4.66:8009
Count:  448 Upstream:  ajp://10.1.3.203:8009
Count:  445 Upstream:  ajp://10.1.3.86:8009
Count:  447 Upstream:  ajp://10.1.3.202:8009
Count:  448 Upstream:  ajp://10.1.4.17:8009
Count:  450 Upstream:  ajp://10.1.3.201:8009
Count:  451 Upstream:  ajp://10.1.4.68:8009
Count:  448 Upstream:  ajp://10.1.3.205:8009
Count:  450 Upstream:  ajp://10.1.4.70:8009
Count:  445 Upstream:  ajp://10.1.4.69:8009
Count:  440 Upstream:  ajp://10.1.4.15:8009
Count:  443 Upstream:  ajp://10.1.3.204:8009
Period: 09:07:24 - 09:08:24
Number of requests for a specified period of time: 6401
Count:  458 Upstream:  ajp://10.1.4.67:8009
Count:  447 Upstream:  ajp://10.1.4.66:8009
Count:  456 Upstream:  ajp://10.1.3.88:8009
Count:  454 Upstream:  ajp://10.1.3.202:8009
Count:  455 Upstream:  ajp://10.1.4.15:8009
Count:  456 Upstream:  ajp://10.1.4.17:8009
Count:  465 Upstream:  ajp://10.1.4.69:8009
Count:  450 Upstream:  ajp://10.1.4.68:8009
Count:  453 Upstream:  ajp://10.1.3.205:8009
Count:  462 Upstream:  ajp://10.1.3.86:8009
Count:  465 Upstream:  ajp://10.1.3.203:8009
Count:  450 Upstream:  ajp://10.1.4.70:8009
Count:  452 Upstream:  ajp://10.1.3.204:8009
Count:  460 Upstream:  ajp://10.1.3.201:8009
Period: 09:08:24 - 09:09:24
Number of requests for a specified period of time: 6984
Count:  498 Upstream:  ajp://10.1.4.68:8009
Count:  495 Upstream:  ajp://10.1.3.204:8009
Count:  495 Upstream:  ajp://10.1.4.66:8009
Count:  506 Upstream:  ajp://10.1.4.70:8009
Count:  498 Upstream:  ajp://10.1.3.205:8009
Count:  503 Upstream:  ajp://10.1.3.88:8009
Count:  494 Upstream:  ajp://10.1.4.15:8009
Count:  512 Upstream:  ajp://10.1.3.202:8009
Count:  514 Upstream:  ajp://10.1.3.86:8009
Count:  485 Upstream:  ajp://10.1.4.69:8009
Count:  494 Upstream:  ajp://10.1.4.17:8009
Count:  488 Upstream:  ajp://10.1.4.67:8009
Count:  495 Upstream:  ajp://10.1.3.203:8009
Count:  488 Upstream:  ajp://10.1.3.201:8009
Period: 09:09:24 - 09:10:24
Number of requests for a specified period of time: 6388
Count:  451 Upstream:  ajp://10.1.3.203:8009
Count:  436 Upstream:  ajp://10.1.3.86:8009
Count:  460 Upstream:  ajp://10.1.3.204:8009
Count:  459 Upstream:  ajp://10.1.3.205:8009
Count:  460 Upstream:  ajp://10.1.3.201:8009
Count:  463 Upstream:  ajp://10.1.4.17:8009
Count:  459 Upstream:  ajp://10.1.4.15:8009
Count:  453 Upstream:  ajp://10.1.4.70:8009
Count:  452 Upstream:  ajp://10.1.3.88:8009
Count:  459 Upstream:  ajp://10.1.4.69:8009
Count:  460 Upstream:  ajp://10.1.4.67:8009
Count:  465 Upstream:  ajp://10.1.4.66:8009
Count:  459 Upstream:  ajp://10.1.4.68:8009
Count:  443 Upstream:  ajp://10.1.3.202:8009
Period: 09:10:24 - 09:11:24
Number of requests for a specified period of time: 6088
Count:  433 Upstream:  ajp://10.1.4.69:8009
Count:  433 Upstream:  ajp://10.1.3.204:8009
Count:  444 Upstream:  ajp://10.1.4.67:8009
Count:  434 Upstream:  ajp://10.1.3.202:8009
Count:  434 Upstream:  ajp://10.1.3.88:8009
Count:  434 Upstream:  ajp://10.1.4.17:8009
Count:  435 Upstream:  ajp://10.1.3.205:8009
Count:  432 Upstream:  ajp://10.1.3.201:8009
Count:  441 Upstream:  ajp://10.1.4.68:8009
Count:  434 Upstream:  ajp://10.1.3.86:8009
Count:  434 Upstream:  ajp://10.1.4.15:8009
Count:  429 Upstream:  ajp://10.1.4.66:8009
Count:  433 Upstream:  ajp://10.1.3.203:8009
Count:  430 Upstream:  ajp://10.1.4.70:8009
Period: 09:11:24 - 09:12:24
Number of requests for a specified period of time: 6480
Count:  462 Upstream:  ajp://10.1.3.204:8009
Count:  452 Upstream:  ajp://10.1.4.67:8009
Count:  479 Upstream:  ajp://10.1.3.88:8009
Count:  465 Upstream:  ajp://10.1.4.69:8009
Count:  459 Upstream:  ajp://10.1.4.66:8009
Count:  460 Upstream:  ajp://10.1.3.86:8009
Count:  464 Upstream:  ajp://10.1.3.202:8009
Count:  462 Upstream:  ajp://10.1.3.201:8009
Count:  467 Upstream:  ajp://10.1.4.15:8009
Count:  464 Upstream:  ajp://10.1.4.70:8009
Count:  463 Upstream:  ajp://10.1.3.203:8009
Count:  460 Upstream:  ajp://10.1.3.205:8009
Count:  452 Upstream:  ajp://10.1.4.68:8009
Count:  459 Upstream:  ajp://10.1.4.17:8009
Period: 09:12:24 - 09:13:24
Number of requests for a specified period of time: 6737
Count:  475 Upstream:  ajp://10.1.4.69:8009
Count:  502 Upstream:  ajp://10.1.4.68:8009
Count:  478 Upstream:  ajp://10.1.3.86:8009
Count:  482 Upstream:  ajp://10.1.4.66:8009
Count:  478 Upstream:  ajp://10.1.3.201:8009
Count:  478 Upstream:  ajp://10.1.3.204:8009
Count:  473 Upstream:  ajp://10.1.3.202:8009
Count:  475 Upstream:  ajp://10.1.4.70:8009
Count:  482 Upstream:  ajp://10.1.4.15:8009
Count:  480 Upstream:  ajp://10.1.3.205:8009
Count:  477 Upstream:  ajp://10.1.4.67:8009
Count:  487 Upstream:  ajp://10.1.3.203:8009
Count:  462 Upstream:  ajp://10.1.3.88:8009
Count:  495 Upstream:  ajp://10.1.4.17:8009
Period: 09:13:24 - 09:14:24
Number of requests for a specified period of time: 6813
Count:  511 Upstream:  ajp://10.1.3.202:8009
Count:  325 Upstream:  ajp://10.1.4.17:8009
Count:  506 Upstream:  ajp://10.1.4.67:8009
Count:  500 Upstream:  ajp://10.1.3.201:8009
Count:  502 Upstream:  ajp://10.1.3.86:8009
Count:  499 Upstream:  ajp://10.1.4.70:8009
Count:  489 Upstream:  ajp://10.1.3.203:8009
Count:  501 Upstream:  ajp://10.1.3.204:8009
Count:  490 Upstream:  ajp://10.1.4.15:8009
Count:  478 Upstream:  ajp://10.1.4.68:8009
Count:  498 Upstream:  ajp://10.1.4.69:8009
Count:  499 Upstream:  ajp://10.1.3.88:8009
Count:  499 Upstream:  ajp://10.1.4.66:8009
Count:  498 Upstream:  ajp://10.1.3.205:8009
Period: 09:14:24 - 09:15:24
Number of requests for a specified period of time: 6629
Count:  475 Upstream:  ajp://10.1.4.66:8009
Count:  472 Upstream:  ajp://10.1.4.68:8009
Count:  473 Upstream:  ajp://10.1.3.204:8009
Count:  475 Upstream:  ajp://10.1.4.69:8009
Count:  465 Upstream:  ajp://10.1.3.202:8009
Count:  471 Upstream:  ajp://10.1.4.67:8009
Count:  473 Upstream:  ajp://10.1.3.88:8009
Count:  474 Upstream:  ajp://10.1.3.201:8009
Count:  477 Upstream:  ajp://10.1.4.70:8009
Count:  473 Upstream:  ajp://10.1.3.203:8009
Count:  472 Upstream:  ajp://10.1.3.205:8009
Count:  474 Upstream:  ajp://10.1.4.15:8009
Count:  470 Upstream:  ajp://10.1.3.86:8009
Count:  461 Upstream:  ajp://10.1.4.17:8009
Period: 09:15:24 - 09:16:24
Number of requests for a specified period of time: 6509
Count:  464 Upstream:  ajp://10.1.3.201:8009
Count:  465 Upstream:  ajp://10.1.3.86:8009
Count:  462 Upstream:  ajp://10.1.3.205:8009
Count:  468 Upstream:  ajp://10.1.4.68:8009
Count:  462 Upstream:  ajp://10.1.4.17:8009
Count:  465 Upstream:  ajp://10.1.3.202:8009
Count:  463 Upstream:  ajp://10.1.4.66:8009
Count:  464 Upstream:  ajp://10.1.3.204:8009
Count:  463 Upstream:  ajp://10.1.3.203:8009
Count:  463 Upstream:  ajp://10.1.4.69:8009
Count:  467 Upstream:  ajp://10.1.3.88:8009
Count:  462 Upstream:  ajp://10.1.4.15:8009
Count:  462 Upstream:  ajp://10.1.4.67:8009
Count:  459 Upstream:  ajp://10.1.4.70:8009
The remainder: 50.0 seconds
Period: 09:16:24 - 09:17:14
Number of requests for a remainder period of time: 5268
Count:  383 Upstream:  ajp://10.1.4.17:8009
Count:  374 Upstream:  ajp://10.1.3.86:8009
Count:  371 Upstream:  ajp://10.1.3.201:8009
Count:  371 Upstream:  ajp://10.1.3.202:8009
Count:  368 Upstream:  ajp://10.1.3.88:8009
Count:  371 Upstream:  ajp://10.1.4.67:8009
Count:  374 Upstream:  ajp://10.1.4.70:8009
Count:  374 Upstream:  ajp://10.1.3.205:8009
Count:  377 Upstream:  ajp://10.1.3.204:8009
Count:  373 Upstream:  ajp://10.1.3.203:8009
Count:  373 Upstream:  ajp://10.1.4.15:8009
Count:  371 Upstream:  ajp://10.1.4.66:8009
Count:  367 Upstream:  ajp://10.1.4.68:8009
Count:  404 Upstream:  ajp://10.1.4.69:8009
The period you specify is: 5.0 minutes
The period you specify is: 300 seconds
Period: 09:01:24 - 09:06:24
Number of requests for a specified period of time: 29425
Count:  2094 Upstream:  ajp://10.1.4.17:8009
Count:  2105 Upstream:  ajp://10.1.4.67:8009
Count:  2095 Upstream:  ajp://10.1.3.201:8009
Count:  2102 Upstream:  ajp://10.1.3.204:8009
Count:  2084 Upstream:  ajp://10.1.4.68:8009
Count:  2104 Upstream:  ajp://10.1.4.15:8009
Count:  2095 Upstream:  ajp://10.1.4.70:8009
Count:  2095 Upstream:  ajp://10.1.3.202:8009
Count:  2095 Upstream:  ajp://10.1.3.203:8009
Count:  2097 Upstream:  ajp://10.1.4.69:8009
Count:  2095 Upstream:  ajp://10.1.3.205:8009
Count:  2092 Upstream:  ajp://10.1.3.88:8009
Count:  2074 Upstream:  ajp://10.1.3.86:8009
Count:  2089 Upstream:  ajp://10.1.4.66:8009
Period: 09:06:24 - 09:11:24
Number of requests for a specified period of time: 32139
Count:  2293 Upstream:  ajp://10.1.3.88:8009
Count:  2292 Upstream:  ajp://10.1.4.67:8009
Count:  2291 Upstream:  ajp://10.1.4.66:8009
Count:  2292 Upstream:  ajp://10.1.3.203:8009
Count:  2291 Upstream:  ajp://10.1.3.86:8009
Count:  2290 Upstream:  ajp://10.1.3.202:8009
Count:  2295 Upstream:  ajp://10.1.4.17:8009
Count:  2290 Upstream:  ajp://10.1.3.201:8009
Count:  2301 Upstream:  ajp://10.1.4.68:8009
Count:  2293 Upstream:  ajp://10.1.3.205:8009
Count:  2290 Upstream:  ajp://10.1.4.70:8009
Count:  2288 Upstream:  ajp://10.1.4.69:8009
Count:  2282 Upstream:  ajp://10.1.4.15:8009
Count:  2283 Upstream:  ajp://10.1.3.204:8009
Period: 09:11:24 - 09:16:24
Number of requests for a specified period of time: 33168
Count:  2378 Upstream:  ajp://10.1.3.204:8009
Count:  2368 Upstream:  ajp://10.1.4.67:8009
Count:  2380 Upstream:  ajp://10.1.3.88:8009
Count:  2377 Upstream:  ajp://10.1.4.69:8009
Count:  2378 Upstream:  ajp://10.1.4.66:8009
Count:  2375 Upstream:  ajp://10.1.3.86:8009
Count:  2378 Upstream:  ajp://10.1.3.202:8009
Count:  2378 Upstream:  ajp://10.1.3.201:8009
Count:  2376 Upstream:  ajp://10.1.4.15:8009
Count:  2374 Upstream:  ajp://10.1.4.70:8009
Count:  2375 Upstream:  ajp://10.1.3.203:8009
Count:  2373 Upstream:  ajp://10.1.3.205:8009
Count:  2373 Upstream:  ajp://10.1.4.68:8009
Count:  2202 Upstream:  ajp://10.1.4.17:8009
The remainder: 50.0 seconds
Period: 09:16:24 - 09:17:14
Number of requests for a remainder period of time: 5268
Count:  383 Upstream:  ajp://10.1.4.17:8009
Count:  374 Upstream:  ajp://10.1.3.86:8009
Count:  371 Upstream:  ajp://10.1.3.201:8009
Count:  371 Upstream:  ajp://10.1.3.202:8009
Count:  368 Upstream:  ajp://10.1.3.88:8009
Count:  371 Upstream:  ajp://10.1.4.67:8009
Count:  374 Upstream:  ajp://10.1.4.70:8009
Count:  374 Upstream:  ajp://10.1.3.205:8009
Count:  377 Upstream:  ajp://10.1.3.204:8009
Count:  373 Upstream:  ajp://10.1.3.203:8009
Count:  373 Upstream:  ajp://10.1.4.15:8009
Count:  371 Upstream:  ajp://10.1.4.66:8009
Count:  367 Upstream:  ajp://10.1.4.68:8009
Count:  404 Upstream:  ajp://10.1.4.69:8009
```
### max_request_frequency(N):
К-во запросов по апстримам (воркерам) вdT (30 сек, 1 минуту, 5 мин).<br>
N = 5.
```
For period = 1 minutes. Number of requests for a specified period of time: 1783
During period: 09:15:51 - 09:16:56
For period = 2 minutes. Number of requests for a specified period of time: 10245
During period: 09:13:38 - 09:15:38
For period = 3 minutes. Number of requests for a specified period of time: 4844
During period: 09:13:28 - 09:16:28
For period = 4 minutes. Number of requests for a specified period of time: 25219
During period: 09:09:24 - 09:13:24
For period = 5 minutes. Number of requests for a specified period of time: 5268
During period: 09:11:24 - 09:16:24
```
