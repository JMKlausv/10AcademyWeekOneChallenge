from loader import *
def make_analysis_on_slack(data_path):
    loader = SlackDataLoader(data_path)
    df = loader.slack_parser()
    
    top_10_reply_count = df.groupby('user')['reply_count'].sum().nlargest(10)
    bottom_10_reply_count = df.groupby('user')['reply_count'].sum().nsmallest(10)
    top_10_mention_count = df.groupby('user')['mention_count'].sum().nlargest(10)
    bottom_10_mention_count = df.groupby('user')['mention_count'].sum().nsmallest(10)
    top_10_message_count = df['user'].value_counts().nlargest(10)
    bottom_10_message_count = df['user'].value_counts().nsmallest(10)
    top_10_reaction_count = df.groupby('user')['reaction_count'].sum().nlargest(10)
    bottom_10_reaction_count = df.groupby('user')['reaction_count'].sum().nsmallest
    
    print("top 10 mention count")
    print(top_10_mention_count.head())
    

   
if __name__ == "__make_analysis_on_slack__":
 # Using the configuration from config.py
    data_path = cfg.path
  
    make_analysis_on_slack(data_path)