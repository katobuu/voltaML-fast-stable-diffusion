![Screenshot from 2022-11-22 15-29-39](https://user-images.githubusercontent.com/107309002/206966210-7e9e57a0-0184-431b-8d28-304c46bce02b.png)


<h1 align="center">🔥 🔥 voltaML-fast-stable-diffusion webUI 🔥 🔥 </h1>

<p align="center">
  <b> Accelerate your machine learning and deep learning models by upto 10X </b> 
</p>

###                                                   

<div align="center">
<a href="https://discord.gg/pY5SVyHmWm"> <img src="https://dcbadge.vercel.app/api/server/pY5SVyHmWm" /> </a> 
</div>


Lightweight library to accelerate Stable-Diffusion, Dreambooth into fastest inference models with **WebUI single click or single line of code**.

<h1 align="center"> Setup webUI </h3>

![Screenshot from 2022-12-12 11-19-09](https://user-images.githubusercontent.com/107309002/206970939-f827f7b9-6966-41c1-a2aa-3ed18e73d399.png)

![Screenshot from 2022-12-12 11-36-37](https://user-images.githubusercontent.com/107309002/206972269-1223c567-3df8-41c5-a7b3-f31e544b98aa.png)


#### Docker setup (if required)
Setup docker on Ubuntu using [these intructions](https://docs.docker.com/engine/install/ubuntu/).

Setup docker on Windows using [these intructions](https://docs.docker.com/desktop/install/windows-install/)


### Launch voltaML container
```
sudo docker run --gpus=all -v $pwd/engine:/workspace/volta_stable_diffusion/engine -it -p "8800:8800" voltaml/volta_stable_diffusion:v0.2
```

