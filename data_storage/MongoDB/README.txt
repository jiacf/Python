
NoSQL，全称Not Only SQL，意为不仅仅是SQL。NoSQL是对于不同于传统的关系型数据库的数据库管理系统的统称。
两者存在愈多显著的不同点，其中最重要的是NoSQL不适用SQL作为查询语言。其数据存储可以不需要固定表格模式，也经常会避免使用SQL的JOIN操作，一般有水平可扩展的特征。
对于爬虫的数据存储来说，一条数据可能存在某些字段提取失败而缺失的情况，而且数据可能随时调整。另外，数据之间还存在嵌套关系，如果使用关系型数据库存储，一是需要提前建表，二是如果存在数据嵌套关系的话，需要进行序列化操作才可以存储，这非常不方便。而这时使用非关系型数据库可以避免一些麻烦，更加高效。