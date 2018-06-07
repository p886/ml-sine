# Learn Sine Function

A neural network learns a sine function.

[COOL VIDEO DEMO MUST WATCH!](https://www.youtube.com/watch/jzYQYGXYPpA)

[How to create these animations](https://philippantar.com/posts/one-way-to-generate-animations-with-keras/)

## Command line options

```
  --skip-images       Do not create plots in img/
```

## Create slideshow movie

```
ffmpeg -n -framerate 4  -i "img/plot_%d.png"  -vf "fps=25,format=yuv420p" movie.mp4
```
