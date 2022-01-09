# video-audio-converters
Python scripts used to convert between various video and audio formats.

## To run
In a command prompt, run the following commands, replacing the text in the "<>" tags.

```bash
	convert_audio_file_type.py <INPUT_DIR> <INPUT_TYPE> <OUTPUT_TYPE>
	convert_video_file_type.py <INPUT_DIR> <INPUT_TYPE> <OUTPUT_TYPE>
```

Here is an example of how that may look.

```bash
	convert_audio_file_type.py example_input_dir wav mp3
	convert_video_file_type.py example_input_dir bik mp4
```

These commands will create output directories named:
* converted_audio_files
* converted_video_files