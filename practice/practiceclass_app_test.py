from practiceclass_blog import PracticeClass
import practiceclass_app
from unittest.mock import patch

practice = PracticeClass()
#practiceclass_app.d = {'Test': practice}
with patch('builtins.print') as mocked_print:
    practiceclass_app.print_practiceclass(practice)
    mocked_print.assert_called_with("Test Class")