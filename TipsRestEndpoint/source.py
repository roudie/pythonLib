import tips.tips_rest
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

APP = Flask(__name__)
API = Api(APP)

API.add_resource(tips.tips_rest.TipsList, '/tips')
API.add_resource(tips.tips_rest.Tip, '/tip/<tip_id>')
API.add_resource(tips.tips_rest.Comment, '/comment/<comment_id>')
API.add_resource(tips.tips_rest.CommentsList, '/comments')


if __name__ == "__main__":
    APP.run(debug=True, host='0.0.0.0', port=4000)
