import pytest


def score(name):
   if name == 'one':
       return 20
   elif name == 'two':
       return 90
   else:
       return 0

@pytest.mark.unit
def test_score():
    """unit test score"""
    print("define mock choices")
    choices = [
        {
            "value": "survey1",
            "score": 20
        },
        {
            "value": "survey2",
            "score": 90
        },
    ]

    print("testing choices")
    score1 = score('one')
    assert score1 == 20, "returns wrong score"
    score2 = score('two')
    assert score2 == 90, "returns wrong score"
    score3 = score('other')
    assert score3 == 0, "returns wrond score"
