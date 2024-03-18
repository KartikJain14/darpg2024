import ffmpeg
def convert_audio(input_file, output_file):
    (
        ffmpeg
        .input(input_file)
        .output(output_file, acodec='pcm_s16le', ac=1, ar='16000', loglevel="quiet")
        .overwrite_output()
        .run()
    )
