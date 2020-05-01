from unittest import TestLoader, TestSuite, TextTestRunner

import unitTest_StaffManageApp
from AdminLoginTest import AdminLoginTest
from AdminManageUser import AdminManageUser
from StaffLoginTest import StaffLoginTest
from AdminManageUsersReport import AdminManageUsersReport
from NurseAccountProfile import NurseAccountProfile
from StaffAccountProfile import StaffAccountProfile
from unitTest_StaffManageApp import StaffManageApp
from ViewNotesStaff import ViewNotesStaff
from ViewNotesNurse import ViewNotesNurse

if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(AdminLoginTest),
        loader.loadTestsFromTestCase(StaffLoginTest),
        loader.loadTestsFromTestCase(AdminManageUser),
        loader.loadTestsFromTestCase(AdminManageUsersReport),
        loader.loadTestsFromTestCase(NurseAccountProfile),
        loader.loadTestsFromTestCase(StaffAccountProfile),
	    loader.loadTestsFromTestCase(unitTest_StaffManageApp.py),
	    loader.loadTestsFromTestCase(unitTest_NurseViewApp.py),
	    loader.loadTestsFromTestCase(StaffAssignNurse.py),
	    loader.loadTestsFromTestCase(ViewNotesStaff),
	    loader.loadTestsFromTestCase(ViewNotesNurse),

    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)