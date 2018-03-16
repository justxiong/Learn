/*************************************************************************
	> File Name: client.c
	> Author:
	> Mail:
	> Created Time: 2018年03月02日 星期五 15时59分13秒
 ************************************************************************/
//learn upd socket
//
#include<stdio.h>

#define BUFFER_SIZE 1328
void net_speed_task(void* arg)
{
	int udpfd;
	char buf[BUFFER_SIZE]={0};
	struct sockaddr_in address;
	char *ip_str = "192.168.8.136";
	int bufferSize;

	bzero(&address,sizeof(address));
	address.sin_family = AF_INET;
	inet_pton(AF_INET,ip_str,&address.sin_addr);
	address.sin_port = htons(6666);
	udpfd = socket(PF_INET,SOCK_DGRAM,0);

	memset(buf,0,BUFFER_SIZE);

	u32 t1 = test_get_micro_sec();
	u32 idx = 0;
	u32 packet_cnt = 0;

	while(1)
	{
		u32 t2 = test_get_micro_sec();
		if(t2-t1<100)
		{
			continue;
		}
		idx++;
		memcpy(buf,&idx,4);
		packet_cnt++;
		if(BUFFER_SIZE != sendto(udpfd,buf,BUFFER_SIZE,0,(struct sockaddr *)&address,sizeof(address)))
		{
			printf("%s line %d sendto error\n",__FUNCTION__,__LINE__);
		}
		u32 t3 = test_get_micro_sec();
		t1 = t3;
		if(packet_cnt>100)
		{
			//printf("%s line %d sleep\n",__FUNCTION__,__LINE__);
			GxCore_ThreadDelay(200);
			packet_cnt = 0;
		}
	}
	close(udpfd);

}

void net_speed_test()
{
	int thread = 0;

	static u8 inited = 0;
	if(inited!=0)
	{
		return;
	}
	inited = 1;
	GxCore_ThreadCreate("net_speed", &thread, net_speed_task, NULL,64*1024,GXOS_DEFAULT_PRIORITY);

}

unsigned int test_get_micro_sec()
{
	GxTime time_now = { 0 };
	unsigned int time_msec = 0;

	GxCore_GetTickTime(&time_now);
	time_msec = time_now.seconds * 1000*1000 + time_now.microsecs;
	//printf("T:%x\n",time_msec);
	return (time_msec);
}
