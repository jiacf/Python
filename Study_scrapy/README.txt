Scrapy��ܵļܹ���
Engine�����棬��������ϵͳ����������������������������ܵĺ��ġ�
Item����Ŀ������������ȡ��������ݽṹ����ȡ�����ݻᱻ��ֵ�ɸ�Item����
Scheduler�����������������淢���������󲢽����������У����������ٴ������ʱ�������ṩ�����档
Downloader����������������ҳ���ݣ�������ҳ���ݷ��ظ�֩�롣
Spiders��֩�룬���ڶ�������ȡ���߼�����ҳ�Ľ�����������Ҫ���������Ӧ��������ȡ������µ�����
Item Pipeline����Ŀ�ܵ�����������֩�����ҳ�г�ȡ����Ŀ��������Ҫ��������ϴ����֤�ʹ洢���ݡ�
Downloader Middlewares���������м����λ�������������֮��Ĺ��ӿ�ܣ���Ҫ����������������֮����������Ӧ��
Spider Middlewares��֩���м����λ�������֩��֮��Ĺ��ӿ�ܣ���Ҫ������֩���������Ӧ������Ľ�����µ�����

2.������
Scrapy�е���������������ƣ��������Ĺ������£�
1.Engine���ȴ�һ����վ���ҵ��������վ��Spider�������Spider�����һ��Ҫ��ȥ��URL��
2.Engine��Spider�л�ȡ����һ��Ҫ��ȥ��URL����ͨ��Scheduler��Request����ʽ���ȡ�
3.Engine��Scheduler������һ��Ҫ��ȥ��URL��
4.Scheduler������һ��Ҫ��ȥ��URL��Engine��Engine��URLͨ��Downloader Middlewaresת����Downloader����
5.һ��ҳ��������ϣ�Downloader���ɸ�ҳ���Response��������ͨ��Downloader Middlewares���͸�Engine��
6.Engine���������н��ܵ�Response��������ͨ��Spider Middlewares���͸�Spider����
7.Spider����Response����������ȡ����Item���µ�Request��Engine
8.Engine��Spider���ص�Item��Item Pipeline�����µ�Request��Scheduler��
9.�ظ���(2)����ֱ��Scheduler��û�и����Request��Engine�رո���վ����ȡ������
