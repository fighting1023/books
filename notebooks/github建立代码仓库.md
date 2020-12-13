# 建立代码仓库
## 1. 登录github创建代码仓库
登录github后，点击页面右上角头像右侧的下三角处，选择`your repositories`
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201213144447908.png)
打开新的页面，点击`New`
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201213144725199.png)
创建代码仓库
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201213145225346.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2NzQ0NjI5,size_16,color_FFFFFF,t_70)
等待一会儿就会跳转到已创建的仓库
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201213145937809.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2NzQ0NjI5,size_16,color_FFFFFF,t_70)


## 2. 删除代码仓库
在项目中进入设置
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020121314585271.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2NzQ0NjI5,size_16,color_FFFFFF,t_70)
进入这个页面
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201213150031950.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2NzQ0NjI5,size_16,color_FFFFFF,t_70)
在这个页面的最下方有
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201213150126530.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2NzQ0NjI5,size_16,color_FFFFFF,t_70)
确认待删除仓库信息
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201213150443567.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzQ2NzQ0NjI5,size_16,color_FFFFFF,t_70)
已删除

## 3. 树莓派安装git

```shell
sudo apt update
```

```shell
sudo apt install git
```
即可完成git的安装

## 4. 将github上的代码仓库拉取到本地

```shell
git clone https的网址
```

```shell
git status
```

```shell
git add .
```

```shell
git commit -m "更新详述"
```

```shell
git pull
```

```shell
git push
```





