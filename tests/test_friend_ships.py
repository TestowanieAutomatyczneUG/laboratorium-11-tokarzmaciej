from unittest import TestCase, main

from src.sample.friendShips import FriendShips


class testFriendShips(TestCase):
    def setUp(self):
        self.temp = FriendShips()

    def test_are_friend(self):
        self.temp.dict = {"Przemek": ["Ala", "Basia", "Piotrek"]}
        self.assertEqual(self.temp.areFriends("Basia", "Przemek"), "Basia is friend Przemek")

    def test_are_not_friend(self):
        self.temp.dict = {"Przemek": ["Ala", "Basia", "Piotrek"]}
        self.assertEqual(self.temp.areFriends("Andrzej", "Przemek"), "Andrzej is not friend Przemek")

    def test_get_friends_list(self):
        self.temp.dict = {"Przemek": ["Ala", "Basia", "Piotrek"]}
        self.assertEqual(self.temp.getFriendsList("Przemek"), ["Ala", "Basia", "Piotrek"])

    def test_get_friends_list_lack_person(self):
        self.temp.dict = {"Przemek": ["Ala", "Basia", "Piotrek"]}
        self.assertRaisesRegex(Exception, "This person not exist", self.temp.getFriendsList, "Adam")

    def test_make_friends(self):
        self.assertEqual(self.temp.makeFriends("Maciek", "Bartek"),
                         {"Maciek": ["Bartek"], "Bartek": ["Maciek"]})

    def test_make_friends_add_friend(self):
        self.temp.dict = {"Przemek": ["Ala"]}
        self.assertEqual(self.temp.makeFriends("Przemek", "Bartek"),
                         {"Przemek": ["Ala","Bartek"], "Bartek": ["Przemek"]})

    def test_make_friend_bad_type(self):
        self.assertRaisesRegex(TypeError, "People have to be type string",
                               self.temp.makeFriends, "Maciek", False)


if __name__ == '__main__':
    main()
