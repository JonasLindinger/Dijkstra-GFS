#!/bin/bash

input="GFS.mp4"
fps=60
numbers=(0 180 270 66 114 180 180 180 360 60 234 1 30 29 1 30 29 1 30 30 30 29 1 30 29 1 30 30 30 29 1 30 30 30 29 1 30 30 30 150 60 120 360 120 180 180 210 120 120 120 320 150 170 90 60 120 120 60 170 120 60 60 120 120 60 60 60 120 120 60 120 840 120 225 180 180 180 240 120 300 60 120 180 300 240 330 840 92 238 180 120 240 720 360 240 360 120 240 120 300 480 120)
count=1

start_frame=${numbers[0]}

for ((i=1; i<${#numbers[@]}; i++)); do
    length=${numbers[i]}

    # Dauer korrekt in Sekunden
    duration=$(printf "%.6f" "$(echo "scale=6; $length / $fps" | bc)")

    # Startzeit in Sekunden
    start_sec=$(printf "%.6f" "$(echo "scale=6; $start_frame / $fps" | bc)")

    ffmpeg -y -ss "$start_sec" -i "$input" -t "$duration" \
        -c:v libx264 -preset veryfast -crf 18 -c:a copy "clip_$count.mp4"

    start_frame=$((start_frame + length))
    ((count++))
done
