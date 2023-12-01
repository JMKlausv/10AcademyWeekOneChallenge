from ..src import loader

def test_columns(path):
    ld = loader.SlackDataLoader(path)
    df = ld.slack_parser()
    expected_columns = ['type', 'text','user','ts','blocks','team','user_team','source_team','user_profile','attachments']  # replace with your expected columns
    assert df.columns.tolist() == expected_columns