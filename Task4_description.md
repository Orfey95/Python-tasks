### count_ip(N):
Собрать статистику по айпишникам браузера, в результате указать N самых частых.<br>
N = 7.
```
Count:  4464 IP address:  54.246.139.111
Count:  4219 IP address:  54.77.132.130
Count:  3170 IP address:  196.11.134.77
Count:  1850 IP address:  41.21.128.106
Count:  1049 IP address:  196.15.209.146
Count:  626 IP address:  196.38.95.108
Count:  534 IP address:  147.110.251.87
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
dT = 3.
```
Total duration of requests: 950.0 seconds
Total duration of requests: 15.833333333333334 minutes
Time of first request: 09:01:24
Time of last request: 09:17:14
The period you specify is: 3 minutes
The period you specify is: 180 seconds
Period: 09:01:24 - 09:04:24
Number of requests for a specified period of time: 17456
Period: 09:04:24 - 09:07:24
Number of requests for a specified period of time: 18247
Error code:  500  Count:  1
Period: 09:07:24 - 09:10:24
Number of requests for a specified period of time: 19773
Period: 09:10:24 - 09:13:24
Number of requests for a specified period of time: 19305
Error code:  500  Count:  9
Period: 09:13:24 - 09:16:24
Number of requests for a specified period of time: 19951
Error code:  500  Count:  10
The remainder: 50.0 seconds
Period: 09:16:24 - 09:17:14
Number of requests for a remainder period of time: 5268
```
### count_max_and_min_link(N):
Найти N самых длинных запросов или самых коротких запросов.<br>
N = 7.
```
The list of links with the minimum length:
Length:    5          Count:     619   URL:       /lite
Length:    5          Count:     1     URL:       /home
Length:    6          Count:     1     URL:       /about
Length:    7          Count:     12    URL:       /mobile
Length:    7          Count:     37    URL:       /search
Length:    9          Count:     3     URL:       /research
Length:    9          Count:     2     URL:       /articles
The list of links with the maximum length:
Length:    1907       Count:     1     URL:       /merlin-service-search/rest/adverts?accessKey=0bca88be-0aab-461a-809b-58d9d045b976&client=ANDROID_SEARCH&pageNumber=0&recordsPerPage=0&id=8a81b5ab4fb5fcb1014fbcb610ff08b6;8a8183204dbb2667014dbe0474b2137e;8a81b6344fb64c9d014fbb313555534f;8a8183224a5f284a014aad873dd659ce;8a8183874df8b5e6014dfb24616e0b9f;8a81b58f4f463b9a014f4a92ce8d362a;8a81b6a74ebb2ca0014ec1c89c1d390c;8a81b3a44e25d464014e2adffc7435a8;8a8183674dbb3f3c014dc39da5eb578e;8a8184db46f2342c0147108c7a615da5;8a81b58e4f835944014f886b1779537e;8a81b5504edae4dd014ef2697ad3647b;8a81b5094edad57d014ef3ec03237ab7;8a81b58e4f5c70a3014f63eadc265157;8a81b64e4f01bcca014f07ae4ae5396d;8a81836748efe6b101499e0339082b91;8a81833a45a8f919014605917ffd7ec7;8a81b5e94fdb8104014fe1da0e0d5a21;8a81833a4532350301454b9a49cc2f21;8a81b64e4f22c9d6014f2bb6188f6dd2;8a8183fe4b2c6cbc014b44344b7044f2;8a8184ae4dbb3c77014dd2bb6dc5793d;8a8183554dbb2ce1014de083ffea17ab;8a81b6624e4b003d014e76f42c1f1c0e;8aa782603dca00cc013dcb16c9ea2ca3;8a8183234a5f11ea014a77d7fd374db7;8a8183cf4cbe2bbd014ce0c584d1741d;8a8184404dbb3d13014dc81268bf1cf8;8a8183554dbb2ce1014dc848ec3f19c3;8a8184fb47abffea0147c46e3fc042ad;8a81b6e74fad0531014fd293ecd3522f;8a8184e14d72c786014d94fd1fa15934;8a8183da4ffd7b69015009b4f12a144d;8a81b6d34f5c43f5014f5facbcac361a;8a81b64e4f2d90f0014f305a6abc0fdf;8a81b22e4e026dbc014e25f37eb215be;8a8184964d283d7a014d33eed24b0df3;8a81b6344fd0a2d0014fd5a5b64e4b5f;8a8184da4cbe2c31014cc24513cf3340;8a81b3094e02689b014e1d18bccb13c0;8a8184554d28022a014d2d3ed9bc3d17;8a81b6d04f73c42a014f86a471644ce7;8a8183324817f16601484516737f16c4;8a8184db46f2342c0146f5a643bf020c;8a81b5184fb636ba014fbbea7b9676d8;8a8183de4c990f9b014ca1e65d763cbb;8a8184dc4cff4b88014d008b405f1704&advertiserId=&channel=&makeModel=&manufactureYear=&price=&mileageInKm=&engineCapacityInCC=&lat=-26.19489&lon=28.04128&distance=&keywords=&bodyType=&advertiserType=&isUsed=&sortBy=&return=resultType%7Cresults%7CnumFound
Length:    1485       Count:     1     URL:       /carandcommercialpricerangeszar/under-10-000/carandcommercialpricerangeszar/10-000-to-24-999/carandcommercialpricerangeszar/25-000-to-39-999/carandcommercialpricerangeszar/40-000-to-54-999/carandcommercialpricerangeszar/55-000-to-69-999/carandcommercialpricerangeszar/70-000-to-84-999/carandcommercialpricerangeszar/85-000-to-99-999/carandcommercialpricerangeszar/100-000-to-124-999/carandcommercialpricerangeszar/125-000-to-149-999/carandcommercialpricerangeszar/150-000-to-174-999/radius/200km/bikeandcarmileageranges/below-1-000-km/bikeandcarmileageranges/1-000-km-to-4-999-km/bikeandcarmileageranges/5-000-km-to-9-999-km/bikeandcarmileageranges/10-000-km-to-19-999-km/bikeandcarmileageranges/20-000-km-to-49-999-km/bikeandcarmileageranges/50-000-km-to-74-999-km/bikeandcarmileageranges/75-000-km-to-99-999-km/carenginecapacityranges/1-6l-to-1-8l/carenginecapacityranges/1-9l-to-2-0l/carenginecapacityranges/2-1l-to-2-5l/makemodel/make/alfa-romeo/makemodel/make/audi/model/a3/makemodel/make/lexus/model/is/makemodel/make/bmw/model/1-series/makemodel/make/mazda/model/3/model/mazda3/makemodel/make/facel-vega/model/other/makemodel/make/opel/model/astra/model/corsa/makemodel/make/ford/model/focus/makemodel/make/hyundai/model/i30/makemodel/make/subaru/model/impreza/makemodel/make/volkswagen/model/golf/model/velociti/makemodel/make/kia/model/cerato/model/koup/model/rio/search?sort=MostRecent&county=KwaZulu-Natal&longitude=31.0292&locationName=Durban&latitude=-29.8579&pageNumber=2
Length:    1484       Count:     1     URL:       /carandcommercialpricerangeszar/under-10-000/carandcommercialpricerangeszar/10-000-to-24-999/carandcommercialpricerangeszar/25-000-to-39-999/carandcommercialpricerangeszar/40-000-to-54-999/carandcommercialpricerangeszar/55-000-to-69-999/carandcommercialpricerangeszar/70-000-to-84-999/carandcommercialpricerangeszar/85-000-to-99-999/carandcommercialpricerangeszar/100-000-to-124-999/carandcommercialpricerangeszar/125-000-to-149-999/carandcommercialpricerangeszar/150-000-to-174-999/radius/200km/bikeandcarmileageranges/below-1-000-km/bikeandcarmileageranges/1-000-km-to-4-999-km/bikeandcarmileageranges/5-000-km-to-9-999-km/bikeandcarmileageranges/10-000-km-to-19-999-km/bikeandcarmileageranges/20-000-km-to-49-999-km/bikeandcarmileageranges/50-000-km-to-74-999-km/bikeandcarmileageranges/75-000-km-to-99-999-km/carenginecapacityranges/1-6l-to-1-8l/carenginecapacityranges/1-9l-to-2-0l/carenginecapacityranges/2-1l-to-2-5l/makemodel/make/alfa-romeo/makemodel/make/audi/model/a3/makemodel/make/lexus/model/is/makemodel/make/bmw/model/1-series/makemodel/make/mazda/model/3/model/mazda3/makemodel/make/facel-vega/model/other/makemodel/make/opel/model/astra/model/corsa/makemodel/make/ford/model/focus/makemodel/make/hyundai/model/i30/makemodel/make/subaru/model/impreza/makemodel/make/volkswagen/model/golf/model/velociti/makemodel/make/kia/model/cerato/model/koup/model/rio/search?sort=MostRecent&gquery=null&locationName=Durban&latitude=-29.8579&longitude=31.0292&county=KwaZulu-Natal
Length:    1482       Count:     2     URL:       /carandcommercialpricerangeszar/under-10-000/carandcommercialpricerangeszar/10-000-to-24-999/carandcommercialpricerangeszar/25-000-to-39-999/carandcommercialpricerangeszar/40-000-to-54-999/carandcommercialpricerangeszar/55-000-to-69-999/carandcommercialpricerangeszar/70-000-to-84-999/carandcommercialpricerangeszar/85-000-to-99-999/carandcommercialpricerangeszar/100-000-to-124-999/carandcommercialpricerangeszar/125-000-to-149-999/carandcommercialpricerangeszar/150-000-to-174-999/radius/200km/bikeandcarmileageranges/below-1-000-km/bikeandcarmileageranges/1-000-km-to-4-999-km/bikeandcarmileageranges/5-000-km-to-9-999-km/bikeandcarmileageranges/10-000-km-to-19-999-km/bikeandcarmileageranges/20-000-km-to-49-999-km/bikeandcarmileageranges/50-000-km-to-74-999-km/bikeandcarmileageranges/75-000-km-to-99-999-km/carenginecapacityranges/1-6l-to-1-8l/carenginecapacityranges/1-9l-to-2-0l/carenginecapacityranges/2-1l-to-2-5l/makemodel/make/alfa-romeo/makemodel/make/audi/model/a3/makemodel/make/lexus/model/is/makemodel/make/bmw/model/1-series/makemodel/make/mazda/model/3/model/mazda3/makemodel/make/facel-vega/model/other/makemodel/make/opel/model/astra/model/corsa/makemodel/make/ford/model/focus/makemodel/make/hyundai/model/i30/makemodel/make/subaru/model/impreza/makemodel/make/volkswagen/model/golf/model/velociti/makemodel/make/kia/model/cerato/model/koup/model/rio/search?sort=PriceAsc&gquery=null&locationName=Durban&latitude=-29.8579&longitude=31.0292&county=KwaZulu-Natal
Length:    1462       Count:     1     URL:       /used-cars/kia/cerato/2012-kia-cerato-koup-2-0-sx-kzn-fpa-8a81848f50381e25015038559d89002e/carandcommercialpricerangeszar/under-10-000/carandcommercialpricerangeszar/10-000-to-24-999/carandcommercialpricerangeszar/25-000-to-39-999/carandcommercialpricerangeszar/40-000-to-54-999/carandcommercialpricerangeszar/55-000-to-69-999/carandcommercialpricerangeszar/70-000-to-84-999/carandcommercialpricerangeszar/85-000-to-99-999/carandcommercialpricerangeszar/100-000-to-124-999/carandcommercialpricerangeszar/125-000-to-149-999/carandcommercialpricerangeszar/150-000-to-174-999/radius/200km/bikeandcarmileageranges/below-1-000-km/bikeandcarmileageranges/1-000-km-to-4-999-km/bikeandcarmileageranges/5-000-km-to-9-999-km/bikeandcarmileageranges/10-000-km-to-19-999-km/bikeandcarmileageranges/20-000-km-to-49-999-km/bikeandcarmileageranges/50-000-km-to-74-999-km/bikeandcarmileageranges/75-000-km-to-99-999-km/carenginecapacityranges/1-6l-to-1-8l/carenginecapacityranges/1-9l-to-2-0l/carenginecapacityranges/2-1l-to-2-5l/makemodel/make/alfa-romeo/makemodel/make/audi/model/a3/makemodel/make/lexus/model/is/makemodel/make/bmw/model/1-series/makemodel/make/mazda/model/3/model/mazda3/makemodel/make/facel-vega/model/other/makemodel/make/opel/model/astra/model/corsa/makemodel/make/ford/model/focus/makemodel/make/hyundai/model/i30/makemodel/make/subaru/model/impreza/makemodel/make/volkswagen/model/golf/model/velociti/makemodel/make/kia/model/cerato/model/koup/model/rio
Length:    1456       Count:     2     URL:       /carandcommercialpricerangeszar/under-10-000/carandcommercialpricerangeszar/10-000-to-24-999/carandcommercialpricerangeszar/25-000-to-39-999/carandcommercialpricerangeszar/40-000-to-54-999/carandcommercialpricerangeszar/55-000-to-69-999/carandcommercialpricerangeszar/70-000-to-84-999/carandcommercialpricerangeszar/85-000-to-99-999/carandcommercialpricerangeszar/100-000-to-124-999/carandcommercialpricerangeszar/125-000-to-149-999/carandcommercialpricerangeszar/150-000-to-174-999/radius/200km/bikeandcarmileageranges/below-1-000-km/bikeandcarmileageranges/1-000-km-to-4-999-km/bikeandcarmileageranges/5-000-km-to-9-999-km/bikeandcarmileageranges/10-000-km-to-19-999-km/bikeandcarmileageranges/20-000-km-to-49-999-km/bikeandcarmileageranges/50-000-km-to-74-999-km/bikeandcarmileageranges/75-000-km-to-99-999-km/carenginecapacityranges/1-6l-to-1-8l/carenginecapacityranges/1-9l-to-2-0l/carenginecapacityranges/2-1l-to-2-5l/makemodel/make/alfa-romeo/makemodel/make/audi/model/a3/makemodel/make/lexus/model/is/makemodel/make/bmw/model/1-series/makemodel/make/mazda/model/3/model/mazda3/makemodel/make/facel-vega/model/other/makemodel/make/opel/model/astra/model/corsa/makemodel/make/ford/model/focus/makemodel/make/hyundai/model/i30/makemodel/make/subaru/model/impreza/makemodel/make/volkswagen/model/golf/model/velociti/makemodel/make/kia/model/cerato/model/koup/model/rio/search?locationName=Durban&latitude=-29.8579&longitude=31.0292&county=KwaZulu-Natal
Length:    1379       Count:     1     URL:       /carandcommercialpricerangeszar/under-10-000/carandcommercialpricerangeszar/10-000-to-24-999/carandcommercialpricerangeszar/25-000-to-39-999/carandcommercialpricerangeszar/40-000-to-54-999/carandcommercialpricerangeszar/55-000-to-69-999/carandcommercialpricerangeszar/70-000-to-84-999/carandcommercialpricerangeszar/85-000-to-99-999/carandcommercialpricerangeszar/100-000-to-124-999/carandcommercialpricerangeszar/125-000-to-149-999/carandcommercialpricerangeszar/150-000-to-174-999/radius/200km/bikeandcarmileageranges/below-1-000-km/bikeandcarmileageranges/1-000-km-to-4-999-km/bikeandcarmileageranges/5-000-km-to-9-999-km/bikeandcarmileageranges/10-000-km-to-19-999-km/bikeandcarmileageranges/20-000-km-to-49-999-km/bikeandcarmileageranges/50-000-km-to-74-999-km/bikeandcarmileageranges/75-000-km-to-99-999-km/carenginecapacityranges/1-6l-to-1-8l/carenginecapacityranges/1-9l-to-2-0l/carenginecapacityranges/2-1l-to-2-5l/makemodel/make/alfa-romeo/makemodel/make/audi/model/a3/makemodel/make/lexus/model/is/makemodel/make/bmw/model/1-series/makemodel/make/mazda/model/3/model/mazda3/makemodel/make/facel-vega/model/other/makemodel/make/opel/model/astra/model/corsa/makemodel/make/ford/model/focus/makemodel/make/hyundai/model/i30/makemodel/make/subaru/model/impreza/makemodel/make/volkswagen/model/golf/model/velociti/makemodel/make/kia/model/cerato/model/koup/model/rio/search
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
К-во запросов по апстримам (воркерам) в dT (30 сек, 1 минуту, 5 мин).<br>
dT = 3.
```
Total duration of requests: 950.0 seconds
Total duration of requests: 15.833333333333334 minutes
Time of first request: 09:01:24
Time of last request: 09:17:14
The period you specify is: 3.0 minutes
The period you specify is: 180 seconds
Period: 09:01:24 - 09:04:24
Number of requests for a specified period of time: 17456
Count:  1236 Upstream:  ajp://10.1.4.70:8009
Count:  1241 Upstream:  ajp://10.1.4.68:8009
Count:  1275 Upstream:  ajp://10.1.4.69:8009
Count:  1240 Upstream:  ajp://10.1.4.67:8009
Count:  1244 Upstream:  ajp://10.1.4.66:8009
Count:  1246 Upstream:  ajp://10.1.4.17:8009
Count:  1244 Upstream:  ajp://10.1.4.15:8009
Count:  1243 Upstream:  ajp://10.1.3.88:8009
Count:  1244 Upstream:  ajp://10.1.3.86:8009
Count:  1245 Upstream:  ajp://10.1.3.205:8009
Count:  1241 Upstream:  ajp://10.1.3.204:8009
Count:  1236 Upstream:  ajp://10.1.3.203:8009
Count:  1230 Upstream:  ajp://10.1.3.202:8009
Count:  1234 Upstream:  ajp://10.1.3.201:8009
Period: 09:04:24 - 09:07:24
Number of requests for a specified period of time: 18247
Count:  1319 Upstream:  ajp://10.1.3.204:8009
Count:  1320 Upstream:  ajp://10.1.3.203:8009
Count:  1326 Upstream:  ajp://10.1.3.202:8009
Count:  1320 Upstream:  ajp://10.1.3.201:8009
Count:  1307 Upstream:  ajp://10.1.4.70:8009
Count:  1306 Upstream:  ajp://10.1.4.69:8009
Count:  1315 Upstream:  ajp://10.1.4.68:8009
Count:  1315 Upstream:  ajp://10.1.4.67:8009
Count:  1311 Upstream:  ajp://10.1.4.66:8009
Count:  1149 Upstream:  ajp://10.1.4.17:8009
Count:  1312 Upstream:  ajp://10.1.4.15:8009
Count:  1311 Upstream:  ajp://10.1.3.88:8009
Count:  1312 Upstream:  ajp://10.1.3.86:8009
Count:  1288 Upstream:  ajp://10.1.3.205:8009
Period: 09:07:24 - 09:10:24
Number of requests for a specified period of time: 19773
Count:  1427 Upstream:  ajp://10.1.4.70:8009
Count:  1416 Upstream:  ajp://10.1.4.69:8009
Count:  1416 Upstream:  ajp://10.1.4.68:8009
Count:  1415 Upstream:  ajp://10.1.4.67:8009
Count:  1416 Upstream:  ajp://10.1.4.66:8009
Count:  1411 Upstream:  ajp://10.1.4.17:8009
Count:  1403 Upstream:  ajp://10.1.4.15:8009
Count:  1405 Upstream:  ajp://10.1.3.88:8009
Count:  1389 Upstream:  ajp://10.1.3.86:8009
Count:  1426 Upstream:  ajp://10.1.3.205:8009
Count:  1404 Upstream:  ajp://10.1.3.204:8009
Count:  1404 Upstream:  ajp://10.1.3.203:8009
Count:  1404 Upstream:  ajp://10.1.3.202:8009
Count:  1404 Upstream:  ajp://10.1.3.201:8009
Period: 09:10:24 - 09:13:24
Number of requests for a specified period of time: 19305
Count:  1379 Upstream:  ajp://10.1.4.17:8009
Count:  1387 Upstream:  ajp://10.1.4.15:8009
Count:  1386 Upstream:  ajp://10.1.3.88:8009
Count:  1382 Upstream:  ajp://10.1.3.86:8009
Count:  1387 Upstream:  ajp://10.1.3.205:8009
Count:  1367 Upstream:  ajp://10.1.3.204:8009
Count:  1379 Upstream:  ajp://10.1.3.203:8009
Count:  1343 Upstream:  ajp://10.1.3.202:8009
Count:  1380 Upstream:  ajp://10.1.3.201:8009
Count:  1375 Upstream:  ajp://10.1.4.70:8009
Count:  1371 Upstream:  ajp://10.1.4.69:8009
Count:  1361 Upstream:  ajp://10.1.4.68:8009
Count:  1377 Upstream:  ajp://10.1.4.67:8009
Count:  1375 Upstream:  ajp://10.1.4.66:8009
Period: 09:13:24 - 09:16:24
Number of requests for a specified period of time: 19951
Count:  1416 Upstream:  ajp://10.1.3.203:8009
Count:  1416 Upstream:  ajp://10.1.3.201:8009
Count:  1412 Upstream:  ajp://10.1.4.70:8009
Count:  1425 Upstream:  ajp://10.1.4.69:8009
Count:  1421 Upstream:  ajp://10.1.4.68:8009
Count:  1416 Upstream:  ajp://10.1.4.67:8009
Count:  1417 Upstream:  ajp://10.1.4.66:8009
Count:  1400 Upstream:  ajp://10.1.4.17:8009
Count:  1403 Upstream:  ajp://10.1.4.15:8009
Count:  1415 Upstream:  ajp://10.1.3.88:8009
Count:  1430 Upstream:  ajp://10.1.3.86:8009
Count:  1414 Upstream:  ajp://10.1.3.205:8009
Count:  1428 Upstream:  ajp://10.1.3.204:8009
Count:  1453 Upstream:  ajp://10.1.3.202:8009
The remainder: 50.0 seconds
Period: 09:16:24 - 09:17:14
Number of requests for a remainder period of time: 5268
Count:  375 Upstream:  ajp://10.1.3.205:8009
Count:  380 Upstream:  ajp://10.1.3.204:8009
Count:  379 Upstream:  ajp://10.1.3.203:8009
Count:  379 Upstream:  ajp://10.1.3.202:8009
Count:  380 Upstream:  ajp://10.1.3.201:8009
Count:  375 Upstream:  ajp://10.1.4.70:8009
Count:  373 Upstream:  ajp://10.1.4.69:8009
Count:  370 Upstream:  ajp://10.1.4.68:8009
Count:  373 Upstream:  ajp://10.1.4.67:8009
Count:  367 Upstream:  ajp://10.1.4.66:8009
Count:  389 Upstream:  ajp://10.1.4.17:8009
Count:  386 Upstream:  ajp://10.1.4.15:8009
Count:  373 Upstream:  ajp://10.1.3.88:8009
Count:  357 Upstream:  ajp://10.1.3.86:8009
```
### max_request_frequency(N, dT):
Найти N периодов времени dT (1 мин, 2 мин, 3 мин и т.д.) за который было выполнено самое большое количество запросов.<br>
N = 6, dT = 3.
```
During period:  09:13:24 - 09:16:24  Count:     19951
During period:  09:07:24 - 09:10:24  Count:     19773
During period:  09:10:24 - 09:13:24  Count:     19305
During period:  09:04:24 - 09:07:24  Count:     18247
During period:  09:01:24 - 09:04:24  Count:     17456
```
