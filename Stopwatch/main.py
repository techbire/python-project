import time

def stopwatch():
    input("Press Enter to start the stopwatch.")
    start_time = time.time()

    try:
        while True:
            elapsed_time = time.time() - start_time
            mins, secs = divmod(elapsed_time, 60)
            hours, mins = divmod(mins, 60)
            time_format = "{:02}:{:02}:{:02}".format(int(hours), int(mins), int(secs))
            print("\rTime elapsed: {}".format(time_format), end="")
            time.sleep(1)

    except KeyboardInterrupt:
        pass  # Catch Ctrl+C to stop the stopwatch

    finally:
        print("\nStopwatch stopped. Total time elapsed: {}".format(time_format))

stopwatch()
