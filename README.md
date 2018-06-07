# Learn Sine Function

<iframe width="560" height="315" src="https://www.youtube.com/embed/jzYQYGXYPpA" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## Command line options

```
  --skip-images       Do not create plots in img/
```

## Create slideshow movie

```
ffmpeg -n -framerate 4  -i "img/plot_%d.png"  -vf "fps=25,format=yuv420p" movie.mp4
```
