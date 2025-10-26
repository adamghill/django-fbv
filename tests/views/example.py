from fbv.decorators import render_view


@render_view()
def three_segment_default(*args):
    return {"value": 789}
