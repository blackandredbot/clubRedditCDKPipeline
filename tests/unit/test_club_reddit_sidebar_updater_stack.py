import aws_cdk as core
import aws_cdk.assertions as assertions

from club_reddit_sidebar_updater.club_reddit_sidebar_updater_stack import (
    ClubRedditSidebarUpdaterStack,
)

# example tests. To run these tests, uncomment this file along with the example
# resource in club_reddit_sidebar_updater/club_reddit_sidebar_updater_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ClubRedditSidebarUpdaterStack(app, "club-reddit-sidebar-updater")
    template = assertions.Template.from_stack(stack)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
