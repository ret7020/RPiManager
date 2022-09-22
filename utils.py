def convert_seconds_to_time_spent(time_raw):
    '''
    Convert seconds to human readable format(used when display uptime)
    '''
    uptime_days = int(time_raw // 86400)
    uptime_hours = int(time_raw // 3600 % 24)
    uptime_minutes = int(time_raw // 60 % 60)
    uptime_seconds = int(time_raw % 60)
    return f"Days: {uptime_days} Hours: {uptime_hours} Minutes: {uptime_minutes} Seconds: {uptime_seconds}"
