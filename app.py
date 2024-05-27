from flask import Flask, render_template, request
from trust_vote_deploy_01 import abi, byteCode, chain_id, myAddress, privateKey, w3
from trust_vote_deploy_02 import DEPLOY, PLACEVOTE, VIEWVOTESTATUS, deployContractOnce
from data import db, OTP, voted_OTP

app = Flask(__name__)

tx_receipt = None
nonce = None
election = None
contract_address = None
flag = True

deployContractOnce()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_form', methods=['POST'])
def process_form():
    name = request.form.get('textinput')
    otp = request.form.get('otpinput')
    vote = request.form.get('vote')
    otp = int(otp)
    vote = int(vote)

    if otp in OTP and otp not in voted_OTP:
        db.insert({"name": name, "vote": vote, "otp": otp})
        PLACEVOTE(vote)
        voted_OTP.append(otp)
        vote_status = VIEWVOTESTATUS()
        return render_template('statusview.html', awl=vote_status[0], bnp=vote_status[1], neutral=vote_status[2],
                               total=vote_status[3])
    else:
        vote_status = VIEWVOTESTATUS()
        return render_template('unsuccessful.html', awl=vote_status[0], bnp=vote_status[1], neutral=vote_status[2],
                               total=vote_status[3])


if __name__ == '__main__':
    app.run(debug=True)
