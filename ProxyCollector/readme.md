此项目由朋友小牛所写一个代理池

启动Proxies.py就可以了

表创建---sql：
CREATE TABLE `pool` (
  `protocol` varchar(5) NOT NULL,
  `host` varchar(30) NOT NULL,
  `port` int(10) NOT NULL,
  `speed` float NOT NULL,
  `isActive` int(11) NOT NULL DEFAULT '1',
  `updateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`host`,`port`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

