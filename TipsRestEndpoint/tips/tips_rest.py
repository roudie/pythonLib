from datetime import datetime
from flask_restful import reqparse, abort, Resource

TIPS = {'0': {'id': 0, 'body': 'body0', 'title': 'title0'},
        '1': {'id': 1, 'body': 'body1', 'title': 'title1'},
        '2': {'id': 2, 'body': 'body2', 'title': 'title2'},
        '4': {'id': 4, 'body': 'body4', 'title': 'title4'}
       }

COMMENTS = {'0': {'id': 0, 'body': 'commentbody0', 'id_tip': 1, 'time': str(datetime.now())}
           }

PARSER_TIP = reqparse.RequestParser()
PARSER_TIP.add_argument('id')
PARSER_TIP.add_argument('body')
PARSER_TIP.add_argument('title')
PARSER_COMMENT = reqparse.RequestParser()
PARSER_COMMENT.add_argument('id')
PARSER_COMMENT.add_argument('body')
PARSER_COMMENT.add_argument('id_tip')
PARSER_COMMENT.add_argument('time')


def abort_if_tip_doesnt_exist(tip_id):
    if tip_id not in TIPS:
        abort(404, message="Tip {} doesn't exist".format(tip_id))


def abort_if_comment_doesnt_exist(comment_id):
    if comment_id not in COMMENTS:
        abort(404, message="Comment {} doesn't exist".format(comment_id))

class Comment(Resource):
    def get(self, comment_id):
        abort_if_comment_doesnt_exist(comment_id)
        return COMMENTS[comment_id]

    def delete(self, comment_id):
        abort_if_comment_doesnt_exist(comment_id)
        del COMMENTS[comment_id]
        return '', 204

    def put(self, comment_id):
        args = PARSER_COMMENT.parse_args()
        print(args)
        abort_if_tip_doesnt_exist(args['id_tip'])
        comment = {
            'id': comment_id,
            'body': args['body'],
            'id_tip': args['id_tip'],
            'time': str(datetime.now())}
        COMMENTS[comment_id] = comment
        return COMMENTS[comment_id]


class CommentsList(Resource):
    def get(self):
        return COMMENTS
    def put(self):
        args = PARSER_COMMENT.parse_args()
        abort_if_tip_doesnt_exist(args['id_tip'])
        comment = {'id': args['id'],
                   'body': args['body'],
                   'id_tip': args['id_tip'],
                   'time': str(datetime.now())}
        COMMENTS[args['id']] = comment
        return COMMENTS[args['id']]


class Tip(Resource):
    def get(self, tip_id):
        abort_if_tip_doesnt_exist(tip_id)
        return TIPS[tip_id]

    def delete(self, tip_id):
        abort_if_tip_doesnt_exist(tip_id)
        del TIPS[tip_id]
        return '', 204

    def put(self, tip_id):
        args = PARSER_TIP.parse_args()
        tip = {'id': args['id'], 'body': args['body'], 'title': args['title']}
        TIPS[tip_id] = tip


class TipsList(Resource):
    def get(self):
        return TIPS
    def put(self):
        args = PARSER_TIP.parse_args()
        tip = {'id': args['id'], 'body': args['body'], 'title': args['title']}
        TIPS[args['id']] = tip
        return TIPS[args['id']]



