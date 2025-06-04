def aggregate_time_series(data_points, bucket_size_seconds):
    """
    Args:
        data_points: List of tuples (timestamp, value) where timestamp is Unix timestamp
        bucket_size_seconds: Size of each time bucket in seconds

    Returns:
        List of tuples (bucket_start_time, average_value)

    Example:
        data = [(1000, 10), (1005, 20), (1010, 30), (1065, 40), (1070, 50)]
        aggregate_time_series(data, 60)  # 60-second buckets
        # Returns: [(1000, 20.0), (1060, 45.0)]
    """

    result = _calc_buckets(data_points[0], data_points[-1], data_points, bucket_size_seconds)
    result = _append_data_points(result, data_points)
    result = _calc_averages(result)

    return _format_output(result)

def _format_output(result):
    output = []
    for item in result:
        tup = (item['start'], item['avg'])
        output.append(tup)

    return output

def _calc_averages(working_result):
    for b in working_result:
        s = sum(b['values'])
        avg = s / len(b['values'])
        b['avg'] = avg

    return working_result

def _append_data_points(working_result, data_points):

    for b in working_result:
        for p in data_points:
            # import pdb; pdb.set_trace()
            if p[0] >= b['start'] and p[0] <= b['end']:
                # we are in the range of this bucket
                b['values'].append(p[1]) #append the point value
    return working_result


def _create_first_bucket(start_time, bucket_size_seconds):
    bucket = { }
    # Generate starting bucket
    # Calculate the bucket start (start time / 60) * 60 = x
    bucket_span_start_time = (start_time // bucket_size_seconds) * bucket_size_seconds
    bucket_span_end_time = bucket_span_start_time + (bucket_size_seconds - 1)

    # create teh bucket span [x  + 59]
    bucket = { }
    bucket['start'] = bucket_span_start_time
    bucket['end'] = bucket_span_end_time
    bucket['values'] = [ ]
    bucket['avg'] = 0

    return bucket

def _create_new_bucket(last_span_end_time, bucket_size_seconds):
    bucket = { }
    bucket_span_start_time = last_span_end_time + 1
    bucket_span_end_time = bucket_span_start_time + bucket_size_seconds - 1
    bucket = { }
    bucket['start'] = bucket_span_start_time
    bucket['end'] = bucket_span_end_time
    bucket['values'] = [ ]
    bucket['avg'] = 0

    return bucket

def _create_all_the_buckets(end_point, first_bucket, bucket_size_seconds):
    buckets = []
    last_span_end_time = first_bucket['end']

    if end_point == first_bucket['start']:
        return buckets

    generate_new_bucket = True
    while generate_new_bucket:
        # import pdb; pdb.set_trace()

        bucket = _create_new_bucket(last_span_end_time, bucket_size_seconds)
        buckets.append(bucket)
        last_span_end_time = bucket['end']

        if end_point <= last_span_end_time:
            generate_new_bucket = False

    return buckets

def _calc_buckets(start_point, end_point, data_points, bucket_size_seconds):
    first_bucket = _create_first_bucket(start_point[0], bucket_size_seconds)
    buckets = []
    buckets.append(first_bucket)

    if len(data_points) > 1:
        buckets = [*buckets, *_create_all_the_buckets(end_point[0], first_bucket, bucket_size_seconds)]

    return buckets

