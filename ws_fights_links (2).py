import requests
from bs4 import BeautifulSoup


events = [
'http://www.ufcstats.com/event-details/ddbd0d6259ce57cc',
'http://www.ufcstats.com/event-details/18f5669a92e99d92',
'http://www.ufcstats.com/event-details/dbd198f780286aca',
'http://www.ufcstats.com/event-details/c32eab6c2119e989',
'http://www.ufcstats.com/event-details/2eab7a6c8b0ed8cc',
'http://www.ufcstats.com/event-details/1e13936d708bcff7',
'http://www.ufcstats.com/event-details/4c12aa7ca246e7a4',
'http://www.ufcstats.com/event-details/14b9e0f2679a2205',
'http://www.ufcstats.com/event-details/dfb965c9824425db',
'http://www.ufcstats.com/event-details/5f8e00c27b7e7410',
'http://www.ufcstats.com/event-details/898337ef520fe4d3',
'http://www.ufcstats.com/event-details/53278852bcd91e11',
'http://www.ufcstats.com/event-details/0b5b6876c2a4723f',
'http://www.ufcstats.com/event-details/fc9a9559a05f2704',
'http://www.ufcstats.com/event-details/33b2f68ef95252e0',
'http://www.ufcstats.com/event-details/5df17b3620145578',
'http://www.ufcstats.com/event-details/b26d3e3746fb4024',
'http://www.ufcstats.com/event-details/44aa652b181bcf68',
'http://www.ufcstats.com/event-details/0c1773639c795466',
'http://www.ufcstats.com/event-details/74fefd43f073cd2f',
'http://www.ufcstats.com/event-details/4565d435005319c0',
'http://www.ufcstats.com/event-details/b09890ba7ce1d1e2',
'http://www.ufcstats.com/event-details/81ca2c245b19b3c5',
'http://www.ufcstats.com/event-details/8d5daf67983b65ba',
'http://www.ufcstats.com/event-details/fd87b1bbfcde9d5e',
'http://www.ufcstats.com/event-details/df05aa15b2d66f57',
'http://www.ufcstats.com/event-details/3ae10ac4df3df05c',
'http://www.ufcstats.com/event-details/0941df56f6ac954b',
'http://www.ufcstats.com/event-details/3cf68c1d17f66af7',
'http://www.ufcstats.com/event-details/1bf49bf829964144',
'http://www.ufcstats.com/event-details/94a5aaf573f780ad',
'http://www.ufcstats.com/event-details/4834ff149dc9542a',
'http://www.ufcstats.com/event-details/a79bfbc01b2264d6',
'http://www.ufcstats.com/event-details/2c104b7e59a72629',
'http://www.ufcstats.com/event-details/70167689d6a01793',
'http://www.ufcstats.com/event-details/e5d03e4d966126bd',
'http://www.ufcstats.com/event-details/03da33a102d9a45f',
'http://www.ufcstats.com/event-details/abcf7e55a0a9ed89',
'http://www.ufcstats.com/event-details/9e0f28d1f639ad73',
'http://www.ufcstats.com/event-details/2f8f3c69522db931',
'http://www.ufcstats.com/event-details/6c9383ffab2725a5',
'http://www.ufcstats.com/event-details/c0c1bc0766df4c00',
'http://www.ufcstats.com/event-details/b16a7e6a627e9789',
'http://www.ufcstats.com/event-details/e31502e3f79d00c5',
'http://www.ufcstats.com/event-details/cbc071cb20ea59c7',
'http://www.ufcstats.com/event-details/6b8f28da9a483049',
'http://www.ufcstats.com/event-details/9de7c97e1c0d7927',
'http://www.ufcstats.com/event-details/351264d11286d09a',
'http://www.ufcstats.com/event-details/c912f676692c353a',
'http://www.ufcstats.com/event-details/7dcf06c1967801c1',
'http://www.ufcstats.com/event-details/b0550072e5f0afa7',
'http://www.ufcstats.com/event-details/9649d75defe0dedb',
'http://www.ufcstats.com/event-details/487c170da059857d',
'http://www.ufcstats.com/event-details/80eacd4da0617c57',
'http://www.ufcstats.com/event-details/e96d8538d3f9d0ed',
'http://www.ufcstats.com/event-details/2d5fbe2103f97053',
'http://www.ufcstats.com/event-details/6546af7ab545b90c',
'http://www.ufcstats.com/event-details/a7a79b8efbceaaac',
'http://www.ufcstats.com/event-details/b5882371e2a3900d',
'http://www.ufcstats.com/event-details/84283233ec42be5f',
'http://www.ufcstats.com/event-details/d4da8995fc91e7ef',
'http://www.ufcstats.com/event-details/c046100aea0dba9a',
'http://www.ufcstats.com/event-details/7a703c565ccaa18f',
'http://www.ufcstats.com/event-details/2a74bbba57058f12',
'http://www.ufcstats.com/event-details/d1d20e651e6cbc02',
'http://www.ufcstats.com/event-details/c7ac79839e86ce33',
'http://www.ufcstats.com/event-details/de25520d54eab12d',
'http://www.ufcstats.com/event-details/aa3153a9941b4d44',
'http://www.ufcstats.com/event-details/42c96a9c4802e2e1',
'http://www.ufcstats.com/event-details/20821819c401ced8',
'http://www.ufcstats.com/event-details/33a331684283900f',
'http://www.ufcstats.com/event-details/1ef0eae31904e534',
'http://www.ufcstats.com/event-details/852454c572675334',
'http://www.ufcstats.com/event-details/8d49545dadf9b919',
'http://www.ufcstats.com/event-details/d5ae8074631762fc',
'http://www.ufcstats.com/event-details/c0342805a1948cbb',
'http://www.ufcstats.com/event-details/03b1e846b09f721d',
'http://www.ufcstats.com/event-details/322a56923b396b4d',
'http://www.ufcstats.com/event-details/4f732e58ed907eff',
'http://www.ufcstats.com/event-details/b45d6b73f4ca4467',
'http://www.ufcstats.com/event-details/35585d970300d45a',
'http://www.ufcstats.com/event-details/8215e4fe24e8e81b',
'http://www.ufcstats.com/event-details/ac5f67109accb482',
'http://www.ufcstats.com/event-details/2eae41f61776c60f',
'http://www.ufcstats.com/event-details/d29b5c4f22c6357d',
'http://www.ufcstats.com/event-details/f5990c11974d8e9c',
'http://www.ufcstats.com/event-details/3144121470023e9a',
'http://www.ufcstats.com/event-details/67ec58d7cf599835',
'http://www.ufcstats.com/event-details/ad99fa5325519169',
'http://www.ufcstats.com/event-details/620be7e0712d431b',
'http://www.ufcstats.com/event-details/49e7e05f902479ca',
'http://www.ufcstats.com/event-details/eed2b71d77d95416',
'http://www.ufcstats.com/event-details/7929be8290289a47',
'http://www.ufcstats.com/event-details/daa89f01e1c0f42a',
'http://www.ufcstats.com/event-details/d181689653115b6a',
'http://www.ufcstats.com/event-details/15515e797aedc137',
'http://www.ufcstats.com/event-details/7cf20446453f852b',
'http://www.ufcstats.com/event-details/602bb270f2bdbf02',
'http://www.ufcstats.com/event-details/02177caefe7c07d4',
'http://www.ufcstats.com/event-details/fc1868f56d3036eb',
'http://www.ufcstats.com/event-details/04076783ca83d6ae',
'http://www.ufcstats.com/event-details/eaa0a728cc91ef60',
'http://www.ufcstats.com/event-details/bcd124bcd3d5be46',
'http://www.ufcstats.com/event-details/9e30f69cc0869301',
'http://www.ufcstats.com/event-details/30e8b4505f5ccf92',
'http://www.ufcstats.com/event-details/e7bc606d269896aa',
'http://www.ufcstats.com/event-details/caced97768818230',
'http://www.ufcstats.com/event-details/d856a0080ac09ed7',
'http://www.ufcstats.com/event-details/a25b71fe5e31fa97',
'http://www.ufcstats.com/event-details/a7724f51e32e763e',
'http://www.ufcstats.com/event-details/d6b68eaf4b68b160',
'http://www.ufcstats.com/event-details/cc5834a495d1ea08',
'http://www.ufcstats.com/event-details/9211aae062b799d6',
'http://www.ufcstats.com/event-details/1979c80150f630c4',
'http://www.ufcstats.com/event-details/d86e913c548c07c2',
'http://www.ufcstats.com/event-details/a3244e3238541482',
'http://www.ufcstats.com/event-details/f4a031ac205ac580',
'http://www.ufcstats.com/event-details/ff9578cdbfabd323',
'http://www.ufcstats.com/event-details/9f3d6ddef3d3cccc',
'http://www.ufcstats.com/event-details/d7907a9a968e4d29',
'http://www.ufcstats.com/event-details/686cccbf1a4de453',
'http://www.ufcstats.com/event-details/23bd78c3f89bdb54',
'http://www.ufcstats.com/event-details/99bf06f20491cb54',
'http://www.ufcstats.com/event-details/353de740bb6c7e75',
'http://www.ufcstats.com/event-details/90e7447d8b7f3f35',
'http://www.ufcstats.com/event-details/1507214bbc7a79e2',
'http://www.ufcstats.com/event-details/1c7cce2f5c17160d',
'http://www.ufcstats.com/event-details/5df10509264586e5',
'http://www.ufcstats.com/event-details/bc7f7f0ba3db74d2',
'http://www.ufcstats.com/event-details/ed069a95aaaf4f56',
'http://www.ufcstats.com/event-details/e7bfdb5e0112891e',
'http://www.ufcstats.com/event-details/c0231720fe516994',
'http://www.ufcstats.com/event-details/47b7e4e60813b7b2',
'http://www.ufcstats.com/event-details/20e403a1acfef130',
'http://www.ufcstats.com/event-details/b4ad3a06ee4d660c',
'http://www.ufcstats.com/event-details/865aa315ea62c511',
'http://www.ufcstats.com/event-details/6a8a06b542e1516d',
'http://www.ufcstats.com/event-details/4512e46543b960ad',
'http://www.ufcstats.com/event-details/46effbd1135423c5',
'http://www.ufcstats.com/event-details/4b2390cfaceb91d8',
'http://www.ufcstats.com/event-details/32541eb5d12668b4',
'http://www.ufcstats.com/event-details/6e3282d57d2467a0',
'http://www.ufcstats.com/event-details/7139cd2ae4bf6a29',
'http://www.ufcstats.com/event-details/bd4389b71fdc0ce2',
'http://www.ufcstats.com/event-details/73e09f837f3b5ecc',
'http://www.ufcstats.com/event-details/5cde96e0a1a1fffe',
'http://www.ufcstats.com/event-details/6810d8d2dd557cf9',
'http://www.ufcstats.com/event-details/4956f60b7fa57c1a',
'http://www.ufcstats.com/event-details/6083f497c22cc075',
'http://www.ufcstats.com/event-details/154a6b3ffae264cd',
'http://www.ufcstats.com/event-details/a196332ee4aa8a82',
'http://www.ufcstats.com/event-details/e18012194473e8b0',
'http://www.ufcstats.com/event-details/d6455cb4bee503ce',
'http://www.ufcstats.com/event-details/2dc7f1762dc0a7ef',
'http://www.ufcstats.com/event-details/2b4faacc16d66898',
'http://www.ufcstats.com/event-details/cfbccfed4e4796fe',
'http://www.ufcstats.com/event-details/5da4e8dc02e50ac0',
'http://www.ufcstats.com/event-details/232c582f29f8f65e',
'http://www.ufcstats.com/event-details/72cbe507644a587c',
'http://www.ufcstats.com/event-details/8a028648f3f0761d',
'http://www.ufcstats.com/event-details/5e7a28f20927d64a',
'http://www.ufcstats.com/event-details/aa5b4eff51bdc7d1',
'http://www.ufcstats.com/event-details/cd42bbe8887bba90',
'http://www.ufcstats.com/event-details/45a2ba3ef82b9700',
'http://www.ufcstats.com/event-details/563d051c9e769b24',
'http://www.ufcstats.com/event-details/ff4c3ab594c7fac3',
'http://www.ufcstats.com/event-details/990060b2a68a7b82',
'http://www.ufcstats.com/event-details/a4bf17bd3ba3423b',
'http://www.ufcstats.com/event-details/a314687f372b2cec',
'http://www.ufcstats.com/event-details/3d481aa374c954a1',
'http://www.ufcstats.com/event-details/e7e970d508529bf3',
'http://www.ufcstats.com/event-details/4887e5bc4dbb73ff',
'http://www.ufcstats.com/event-details/e60201cfab7d656d',
'http://www.ufcstats.com/event-details/db1f2ed63b54b9a7',
'http://www.ufcstats.com/event-details/39c568f8c579913e',
'http://www.ufcstats.com/event-details/d56bb6dff2ae77eb',
'http://www.ufcstats.com/event-details/de99da2c0d18d34a',
'http://www.ufcstats.com/event-details/b3fb8d2293e17a59',
'http://www.ufcstats.com/event-details/c6becb722706c7d8',
'http://www.ufcstats.com/event-details/380e8b023290d091',
'http://www.ufcstats.com/event-details/80d918336163b80c',
'http://www.ufcstats.com/event-details/354808cf38d9d73c',
'http://www.ufcstats.com/event-details/20fbff570c678e1c',
'http://www.ufcstats.com/event-details/dd39f1ca787a3d9d',
'http://www.ufcstats.com/event-details/4d636c3aa1105950',
'http://www.ufcstats.com/event-details/243b07fc65ccbb16',
'http://www.ufcstats.com/event-details/8d04923f2db59b7f',
'http://www.ufcstats.com/event-details/5345f86680378fc1',
'http://www.ufcstats.com/event-details/f3155a94ca420126',
'http://www.ufcstats.com/event-details/119ebea97e914dcf',
'http://www.ufcstats.com/event-details/a4dd5c9a75763295',
'http://www.ufcstats.com/event-details/82f5c81f4e3c3eb5',
'http://www.ufcstats.com/event-details/2ce6541127b0e232',
'http://www.ufcstats.com/event-details/b71667c778b6d9e5',
'http://www.ufcstats.com/event-details/a9c45a8b21eabadc',
'http://www.ufcstats.com/event-details/0c3838c8f7c620c2',
'http://www.ufcstats.com/event-details/ef7fa30364cbe7f2',
'http://www.ufcstats.com/event-details/36877f0e62b25b96',
'http://www.ufcstats.com/event-details/a890f9a791ed615d',
'http://www.ufcstats.com/event-details/3be081c29bf734d9',
'http://www.ufcstats.com/event-details/86e388ed20761ad9',
'http://www.ufcstats.com/event-details/194fc025f9355db6',
'http://www.ufcstats.com/event-details/a58114c6dd0add64',
'http://www.ufcstats.com/event-details/06dc1a58663579d2',
'http://www.ufcstats.com/event-details/aae0897825336b1a',
'http://www.ufcstats.com/event-details/4f7e290e71d60f87',
'http://www.ufcstats.com/event-details/b1605ea39fba6af6',
'http://www.ufcstats.com/event-details/8a1b4330c7957961',
'http://www.ufcstats.com/event-details/997b4f52f76a0b53',
'http://www.ufcstats.com/event-details/bc7cf284c1c2f16e',
'http://www.ufcstats.com/event-details/5de61b03868035ff',
'http://www.ufcstats.com/event-details/16d09e800ad7ec79',
'http://www.ufcstats.com/event-details/fa534853eb195270',
'http://www.ufcstats.com/event-details/f54200f1dfb9b5d4',
'http://www.ufcstats.com/event-details/ad4e9055bf8cd04d',
'http://www.ufcstats.com/event-details/0577808d22dfe79c',
'http://www.ufcstats.com/event-details/f9c7fe2682af3802',
'http://www.ufcstats.com/event-details/43563a32c3f10e95',
'http://www.ufcstats.com/event-details/706404da0775dcbc',
'http://www.ufcstats.com/event-details/f9aa6376ae16bfb4',
'http://www.ufcstats.com/event-details/a72d260b436924c4',
'http://www.ufcstats.com/event-details/4e5bbc4566049cbf',
'http://www.ufcstats.com/event-details/d4a12dfa4067742f',
'http://www.ufcstats.com/event-details/222d6b547de2e035',
'http://www.ufcstats.com/event-details/dfdd0c5dd0d4bc23',
'http://www.ufcstats.com/event-details/155a02a8b4311057',
'http://www.ufcstats.com/event-details/59851163aaf1aed8',
'http://www.ufcstats.com/event-details/6ca68b636fbc1f18',
'http://www.ufcstats.com/event-details/371a1c91b24dec2b',
'http://www.ufcstats.com/event-details/53f02bbc41d99432',
'http://www.ufcstats.com/event-details/0313bf497de9c470',
'http://www.ufcstats.com/event-details/8dc4f34c1f50d00d',
'http://www.ufcstats.com/event-details/3bb030257966b022',
'http://www.ufcstats.com/event-details/2dea80c069847321',
'http://www.ufcstats.com/event-details/a71feb7ea7592a71',
'http://www.ufcstats.com/event-details/9bcfb40dbcd50568',
'http://www.ufcstats.com/event-details/269d103c96a4c3a5',
'http://www.ufcstats.com/event-details/063649e21bc9d6d5',
'http://www.ufcstats.com/event-details/770b9d4813c25902',
'http://www.ufcstats.com/event-details/fd7acf42bd6e7e95',
'http://www.ufcstats.com/event-details/05fbfe628658c538',
'http://www.ufcstats.com/event-details/073eee4e62f0d988',
'http://www.ufcstats.com/event-details/79ded75550efc139',
'http://www.ufcstats.com/event-details/1c5879330d42255f',
'http://www.ufcstats.com/event-details/53adf5b845d91e4a',
'http://www.ufcstats.com/event-details/c0ed7b208197e8de',
'http://www.ufcstats.com/event-details/ac9521250dc1a14c',
'http://www.ufcstats.com/event-details/5b5307450405abf0',
'http://www.ufcstats.com/event-details/1fcfc3709fe58151',
'http://www.ufcstats.com/event-details/59aaf2730b84698a',
'http://www.ufcstats.com/event-details/b757c73f443d4fca',
'http://www.ufcstats.com/event-details/9ca265dfe8323db3',
'http://www.ufcstats.com/event-details/579fcdfcabd23a7b',
'http://www.ufcstats.com/event-details/4f2fcbefb668689d',
'http://www.ufcstats.com/event-details/a421465acbe59c77',
'http://www.ufcstats.com/event-details/f9f07bb5a43535ed',
'http://www.ufcstats.com/event-details/d632d156c0549e07',
'http://www.ufcstats.com/event-details/d5f820c11a121050',
'http://www.ufcstats.com/event-details/179f1948dc234f1f',
'http://www.ufcstats.com/event-details/ebc1f40e00e0c481',
'http://www.ufcstats.com/event-details/a26198ba5093147e',
'http://www.ufcstats.com/event-details/3138fab619faf4d1',
'http://www.ufcstats.com/event-details/51b0bb73a1da34bc',
'http://www.ufcstats.com/event-details/fc31f896cde2bc2e',
'http://www.ufcstats.com/event-details/a8d521d913df4e31',
'http://www.ufcstats.com/event-details/30a09e43f15f1d75',
'http://www.ufcstats.com/event-details/e5c9de15bb58b1c6',
'http://www.ufcstats.com/event-details/83d0de122f2f9664',
'http://www.ufcstats.com/event-details/480b702debcb5433',
'http://www.ufcstats.com/event-details/ee457ef1e1c326c1',
'http://www.ufcstats.com/event-details/9a967e8e43dcef63',
'http://www.ufcstats.com/event-details/28f3c2258a1d8874',
'http://www.ufcstats.com/event-details/5d7c18191b8aa432',
'http://www.ufcstats.com/event-details/35dc6220b113b7ec',
'http://www.ufcstats.com/event-details/60884f31ead1609c',
'http://www.ufcstats.com/event-details/eae4aec1a5a8ff01',
'http://www.ufcstats.com/event-details/43612456979e5d5e',
'http://www.ufcstats.com/event-details/df5a77121ba84a5d',
'http://www.ufcstats.com/event-details/b23fca14c7b79935',
'http://www.ufcstats.com/event-details/980b4e712489098e',
'http://www.ufcstats.com/event-details/e5c38954c006f15c',
'http://www.ufcstats.com/event-details/cf1a88371c8cb690',
'http://www.ufcstats.com/event-details/ebc5af72ad5a28cb',
'http://www.ufcstats.com/event-details/5330fe7e4c3af81c',
'http://www.ufcstats.com/event-details/e0b74df14f52cd15',
'http://www.ufcstats.com/event-details/8fd1f27e86661ede',
'http://www.ufcstats.com/event-details/7865707fd684d77b',
'http://www.ufcstats.com/event-details/3c241737a6069b9f',
'http://www.ufcstats.com/event-details/030f08370fd1c2bb',
'http://www.ufcstats.com/event-details/ea0ad155451ed1f5',
'http://www.ufcstats.com/event-details/aa79d5399571068e',
'http://www.ufcstats.com/event-details/ce47f49e5c386a9c',
'http://www.ufcstats.com/event-details/6291ac0a3726732f',
'http://www.ufcstats.com/event-details/f1b2a4365799c48b',
'http://www.ufcstats.com/event-details/83c6c3e0f8bde8ee',
'http://www.ufcstats.com/event-details/09c44b317c98bf96',
'http://www.ufcstats.com/event-details/4679a38cced7c64a',
'http://www.ufcstats.com/event-details/601cf40c09090853',
'http://www.ufcstats.com/event-details/738acab0c6934dd8',
'http://www.ufcstats.com/event-details/56f4b81ec4db61af',
'http://www.ufcstats.com/event-details/c6e6926a81adcd00',
'http://www.ufcstats.com/event-details/c6da1c24fe473418',
'http://www.ufcstats.com/event-details/e8c170a64dc920ac',
'http://www.ufcstats.com/event-details/d1e6a6536ee62517',
'http://www.ufcstats.com/event-details/d41937647eae9a34',
'http://www.ufcstats.com/event-details/319fa1bd3176bded',
'http://www.ufcstats.com/event-details/96d173b7f92aa520',
'http://www.ufcstats.com/event-details/6a0b80a24f22e152',
'http://www.ufcstats.com/event-details/6cbb7661c3258617',
'http://www.ufcstats.com/event-details/53e533db1b8e9712',
'http://www.ufcstats.com/event-details/3c48019bc387b80c',
'http://www.ufcstats.com/event-details/f62850b3c7480db9',
'http://www.ufcstats.com/event-details/abbc4fc02e0d84b3',
'http://www.ufcstats.com/event-details/d3b5ad3b15a64a18',
'http://www.ufcstats.com/event-details/e8efeb9cf33b1941',
'http://www.ufcstats.com/event-details/3da19339ee7051d5',
'http://www.ufcstats.com/event-details/505934897b8b4824',
'http://www.ufcstats.com/event-details/49590e0508b2c19f',
'http://www.ufcstats.com/event-details/96087e90d900f0ef',
'http://www.ufcstats.com/event-details/4985113c0928aa62',
'http://www.ufcstats.com/event-details/8caca5857ce0e30b',
'http://www.ufcstats.com/event-details/5898357a45a73674',
'http://www.ufcstats.com/event-details/155bfc7ed36622df',
'http://www.ufcstats.com/event-details/21f2974fd08085e3',
'http://www.ufcstats.com/event-details/b5ea750025697880',
'http://www.ufcstats.com/event-details/8377c5572cb356f3',
'http://www.ufcstats.com/event-details/0a97691039c4bbfb',
'http://www.ufcstats.com/event-details/df2cf66d8c0123db',
'http://www.ufcstats.com/event-details/c3c23c99477c041b',
'http://www.ufcstats.com/event-details/4d74641fac830182',
'http://www.ufcstats.com/event-details/18524b46c570730b',
'http://www.ufcstats.com/event-details/91720876db0ee468',
'http://www.ufcstats.com/event-details/6d7886b094b471ac',
'http://www.ufcstats.com/event-details/1f5f75658551f2d3',
'http://www.ufcstats.com/event-details/0ec821423baa26bd',
'http://www.ufcstats.com/event-details/1c061eb6e29eaa0a',
'http://www.ufcstats.com/event-details/e780ccc79a209985',
'http://www.ufcstats.com/event-details/8788beb528894f33',
'http://www.ufcstats.com/event-details/7d5b12de1625984e',
'http://www.ufcstats.com/event-details/44f9c777fed7ca03',
'http://www.ufcstats.com/event-details/73ef22f25d0f70e2',
'http://www.ufcstats.com/event-details/1ffc38f67785797b',
'http://www.ufcstats.com/event-details/18968f97ad34f15c',
'http://www.ufcstats.com/event-details/4c8d6fde2dde07c4',
'http://www.ufcstats.com/event-details/f1f9e48a0d150757',
'http://www.ufcstats.com/event-details/83fd97284f4bb4a4',
'http://www.ufcstats.com/event-details/d023ae89a2a4a41e',
'http://www.ufcstats.com/event-details/aac5ac38148f0528',
'http://www.ufcstats.com/event-details/3ba3b5cc94498437',
'http://www.ufcstats.com/event-details/b732b326c362fb62',
'http://www.ufcstats.com/event-details/2db7fa8db6bc9632',
'http://www.ufcstats.com/event-details/8a59d346dc976a10',
'http://www.ufcstats.com/event-details/1411c630ba711b64',
'http://www.ufcstats.com/event-details/a54fc2d6fc224dc3',
'http://www.ufcstats.com/event-details/88a9bc81271ccd89',
'http://www.ufcstats.com/event-details/65ddc8a9ac4e8531',
'http://www.ufcstats.com/event-details/282fa667ff9c51ed',
'http://www.ufcstats.com/event-details/d1152823307d7e7c',
'http://www.ufcstats.com/event-details/132f860d02953f4c',
'http://www.ufcstats.com/event-details/5d7bdab5e03e3216',
'http://www.ufcstats.com/event-details/dd992d569aaebee6',
'http://www.ufcstats.com/event-details/0ff11cc094e887bc',
'http://www.ufcstats.com/event-details/afdb76fbd86f6d11',
'http://www.ufcstats.com/event-details/d512d9f204059f57',
'http://www.ufcstats.com/event-details/ad32471f01e7b1a5',
'http://www.ufcstats.com/event-details/acff437707625fc7',
'http://www.ufcstats.com/event-details/054defd5420a551f',
'http://www.ufcstats.com/event-details/2f3f12002564bb55',
'http://www.ufcstats.com/event-details/f12f979b657ab876',
'http://www.ufcstats.com/event-details/140745cbbcb023ac',
'http://www.ufcstats.com/event-details/9bcf8603ceb25680',
'http://www.ufcstats.com/event-details/cfb65863d5099327',
'http://www.ufcstats.com/event-details/bfc2fc38a0e20211',
'http://www.ufcstats.com/event-details/d0c29452d3272603',
'http://www.ufcstats.com/event-details/24b033b3daf1c9df',
'http://www.ufcstats.com/event-details/3ed134d85dfbd7b4',
'http://www.ufcstats.com/event-details/c80095f6092271a7',
'http://www.ufcstats.com/event-details/3795fca327cbcf23',
'http://www.ufcstats.com/event-details/49efbdc6c9f650c4',
'http://www.ufcstats.com/event-details/15edcf67ccf5be84',
'http://www.ufcstats.com/event-details/58bc81376286b3d3',
'http://www.ufcstats.com/event-details/a6d8bfe9e0c8153b',
'http://www.ufcstats.com/event-details/821cd80aab70d5f9',
'http://www.ufcstats.com/event-details/91d73ee59347ac16',
'http://www.ufcstats.com/event-details/84a067c46306a737',
'http://www.ufcstats.com/event-details/fa8b9e6b0c2269f8',
'http://www.ufcstats.com/event-details/7c0847d3854a95f2',
'http://www.ufcstats.com/event-details/896c322f56b8be5a',
'http://www.ufcstats.com/event-details/a8ea84cbe1655f0a',
'http://www.ufcstats.com/event-details/c6a33ff198aaaeeb',
'http://www.ufcstats.com/event-details/48d1f690b763934c',
'http://www.ufcstats.com/event-details/0ee783aa00e468f0',
'http://www.ufcstats.com/event-details/4908c5ee68a50ee5',
'http://www.ufcstats.com/event-details/cb6783c39c01d896',
'http://www.ufcstats.com/event-details/c4b6099f0d25f75e',
'http://www.ufcstats.com/event-details/1652f3213655b935',
'http://www.ufcstats.com/event-details/04d5718ed2661e8c',
'http://www.ufcstats.com/event-details/29b5791e51e7e832',
'http://www.ufcstats.com/event-details/7d21de9c6d7c98b2',
'http://www.ufcstats.com/event-details/d1759b2b7be9be56',
'http://www.ufcstats.com/event-details/2a542ee8a8b83559',
'http://www.ufcstats.com/event-details/68c6cd5287b473a7',
'http://www.ufcstats.com/event-details/23ab42947c1990e3',
'http://www.ufcstats.com/event-details/ea398c802d9998ee',
'http://www.ufcstats.com/event-details/30cd319d39ee689b',
'http://www.ufcstats.com/event-details/a2b06ca02bca14c0',
'http://www.ufcstats.com/event-details/c670aa48827d6be6',
'http://www.ufcstats.com/event-details/312f47c3d2f83ffa',
'http://www.ufcstats.com/event-details/279093302a6f44b3',
'http://www.ufcstats.com/event-details/0db70ca89e1c7374',
'http://www.ufcstats.com/event-details/19ffeb5e3fffd6d5',
'http://www.ufcstats.com/event-details/46f11d15c0134fe3',
'http://www.ufcstats.com/event-details/bf12aca029bfcc47',
'http://www.ufcstats.com/event-details/2299605af59fd309',
'http://www.ufcstats.com/event-details/2efbc83a6b9b7f86',
'http://www.ufcstats.com/event-details/2549d63da9c456cb',
'http://www.ufcstats.com/event-details/ad047e3073a775f3',
'http://www.ufcstats.com/event-details/b9e871af730f826c',
'http://www.ufcstats.com/event-details/598a58db87b890ee',
'http://www.ufcstats.com/event-details/597db668b01c442c',
'http://www.ufcstats.com/event-details/33e33d51f289d2a1',
'http://www.ufcstats.com/event-details/a24e080000fa7a35',
'http://www.ufcstats.com/event-details/7269329bd87eb479',
'http://www.ufcstats.com/event-details/df85d6ec3493d120',
'http://www.ufcstats.com/event-details/1d147d4163a6989b',
'http://www.ufcstats.com/event-details/91181b29be041f1c',
'http://www.ufcstats.com/event-details/bad28b7b34f334de',
'http://www.ufcstats.com/event-details/f341f9551ba744e2',
'http://www.ufcstats.com/event-details/0aa92558424ced9e',
'http://www.ufcstats.com/event-details/a5c53b3ddb31cc7d',
'http://www.ufcstats.com/event-details/2a6f8136da1e52c0',
'http://www.ufcstats.com/event-details/e7ec11096eac0282',
'http://www.ufcstats.com/event-details/5ca158b1cc9cb242',
'http://www.ufcstats.com/event-details/304fcd812f12c589',
'http://www.ufcstats.com/event-details/2e04a3b4a2011b97',
'http://www.ufcstats.com/event-details/4604ab1de9058474',
'http://www.ufcstats.com/event-details/c1684f00c626f4c0',
'http://www.ufcstats.com/event-details/a6c2f5381d575920',
'http://www.ufcstats.com/event-details/de3ed2e152520c8d',
'http://www.ufcstats.com/event-details/63b65af1c5cb02cb',
'http://www.ufcstats.com/event-details/13c4313ed0f744f3',
'http://www.ufcstats.com/event-details/ee5df903f80c6816',
'http://www.ufcstats.com/event-details/21b8a0f5c231096f',
'http://www.ufcstats.com/event-details/3fed746acfd026dd',
'http://www.ufcstats.com/event-details/baf942f4bcb09894',
'http://www.ufcstats.com/event-details/13b2f59210dda9cc',
'http://www.ufcstats.com/event-details/577ec7e108b94be3',
'http://www.ufcstats.com/event-details/13e62d766b709aa6',
'http://www.ufcstats.com/event-details/f717b6002486f73f',
'http://www.ufcstats.com/event-details/46c8ec317aff28ac',
'http://www.ufcstats.com/event-details/f70144caea5c4c80',
'http://www.ufcstats.com/event-details/445a98acb8985970',
'http://www.ufcstats.com/event-details/1dab0d1d81dd06db',
'http://www.ufcstats.com/event-details/a54a35a670d8e852',
'http://www.ufcstats.com/event-details/03688dc3c3af3ac1',
'http://www.ufcstats.com/event-details/b361180739bed4b0',
'http://www.ufcstats.com/event-details/0e9869d712e81f8f',
'http://www.ufcstats.com/event-details/977081bc01197656',
'http://www.ufcstats.com/event-details/2ee09ec2a0695eb9',
'http://www.ufcstats.com/event-details/c7e9d15cfce52f1d',
'http://www.ufcstats.com/event-details/31ceaf0e670c1578',
'http://www.ufcstats.com/event-details/271fe91f4ba9d2c5',
'http://www.ufcstats.com/event-details/efaf544314bb5c2e',
'http://www.ufcstats.com/event-details/669a3cb6e394f515',
'http://www.ufcstats.com/event-details/3f24c96753dbd9f9',
'http://www.ufcstats.com/event-details/d3711d3784b76255',
'http://www.ufcstats.com/event-details/c933d423ebdbbbdb',
'http://www.ufcstats.com/event-details/fbbde91f7bc2d3c5',
'http://www.ufcstats.com/event-details/85d905f7c4f5a1af',
'http://www.ufcstats.com/event-details/ce783bf73b5131f9',
'http://www.ufcstats.com/event-details/b4bc2e3353a770b5',
'http://www.ufcstats.com/event-details/429e7d3725852ce9',
'http://www.ufcstats.com/event-details/e8fb8e53bc2e29d6',
'http://www.ufcstats.com/event-details/94609dd91731d428',
'http://www.ufcstats.com/event-details/e670f8cc2969a789',
'http://www.ufcstats.com/event-details/c61f66d8c3fd5f07',
'http://www.ufcstats.com/event-details/108afe61a26bcbf4',
'http://www.ufcstats.com/event-details/ae58685caf8e4a0d',
'http://www.ufcstats.com/event-details/bba678d312590087',
'http://www.ufcstats.com/event-details/e06fd1260ac865a7',
'http://www.ufcstats.com/event-details/0cf935519d439ba6',
'http://www.ufcstats.com/event-details/1dc56b59cb28425d',
'http://www.ufcstats.com/event-details/9ccdd2ce45903f34',
'http://www.ufcstats.com/event-details/9fd1f08dd4aec14a',
'http://www.ufcstats.com/event-details/02fc8f50f56eb307',
'http://www.ufcstats.com/event-details/946f341df6472ee0',
'http://www.ufcstats.com/event-details/4dc496aa0cfc0d95',
'http://www.ufcstats.com/event-details/c75b99887c8c3f5a',
'http://www.ufcstats.com/event-details/7b9aa973e5c04624',
'http://www.ufcstats.com/event-details/20bd6c3e03c46ee6',
'http://www.ufcstats.com/event-details/2b1587a3376ab743',
'http://www.ufcstats.com/event-details/08ae5cd9aef7ddd3',
'http://www.ufcstats.com/event-details/da6dfd09cca1d705',
'http://www.ufcstats.com/event-details/31652c9267606d54',
'http://www.ufcstats.com/event-details/cedfdf8d423d500c',
'http://www.ufcstats.com/event-details/d2b1c1317a39f6c6',
'http://www.ufcstats.com/event-details/20ec0061400178ca',
'http://www.ufcstats.com/event-details/a8fa0c4e95512806',
'http://www.ufcstats.com/event-details/afaad7d6a581e307',
'http://www.ufcstats.com/event-details/1a1a4d7a29041d77',
'http://www.ufcstats.com/event-details/a7b48e18ca27795d',
'http://www.ufcstats.com/event-details/a220be6d41d6f97d',
'http://www.ufcstats.com/event-details/c9bbf1a0285a8076',
'http://www.ufcstats.com/event-details/32a3025d5db456ae',
'http://www.ufcstats.com/event-details/4a01dc8376736ef5',
'http://www.ufcstats.com/event-details/749685d24e2cac50',
'http://www.ufcstats.com/event-details/29f935654825331b',
'http://www.ufcstats.com/event-details/07a18ae55dfc3cd9',
'http://www.ufcstats.com/event-details/dc950d59dc590aca',
'http://www.ufcstats.com/event-details/5bd533d50c8e7b8a',
'http://www.ufcstats.com/event-details/96eff1a628adcc7f',
'http://www.ufcstats.com/event-details/9b5b5a75523728f3',
'http://www.ufcstats.com/event-details/6ceff86fae4f6b3b',
'http://www.ufcstats.com/event-details/aee8eecfc4bfb1e7',
'http://www.ufcstats.com/event-details/a390eb8a9b2df298',
'http://www.ufcstats.com/event-details/b63e800c18e011b5',
'http://www.ufcstats.com/event-details/31bbd46d57dfbcb7',
'http://www.ufcstats.com/event-details/5af480a3b2e1726b',
'http://www.ufcstats.com/event-details/1c3f5e85b59ec710',
'http://www.ufcstats.com/event-details/dedc3bb440d09554',
'http://www.ufcstats.com/event-details/b60391da771deefe',
'http://www.ufcstats.com/event-details/1a49e0670dfaca31',
'http://www.ufcstats.com/event-details/a6a9ab5a824e8f66',
'http://www.ufcstats.com/event-details/6420efac0578988b',
]


lutas = []

for i in range(len(events)):
    page = requests.get(events[i])

    soup = BeautifulSoup(page.text, 'html.parser')

    tabela_links = soup.find(class_='b-fight-details__table-body')
    
    lutas.append(tabela_links.prettify())
