from unittest import TestCase, main
from unittest.mock import *
from src.sample.friendShips import FriendShips
from src.sample.friendShipsStorage import FriendStorage


class testFriendShipsStorage(TestCase):

    def test_are_friend(self):
        objectFriend = FriendShips()
        objectFriend.dict = {"Przemek": ["Ala", "Basia", "Piotrek"]}
        objectFriend.areFriends = MagicMock()
        objectFriend.areFriends.return_value = "Basia is friend Przemek"

        objectStorage = FriendStorage()
        objectStorage.storage = objectFriend
        result = objectStorage.areFriends("Basia", "Przemek")

        self.assertEqual(result, "Basia is friend Przemek")

    def test_are_not_friend(self):
        objectFriend = FriendShips()
        objectFriend.dict = {"Przemek": ["Ala", "Basia", "Piotrek"]}
        objectFriend.areFriends = MagicMock()
        objectFriend.areFriends.return_value = "Andrzej is not friend Przemek"

        objectStorage = FriendStorage()
        objectStorage.storage = objectFriend
        result = objectStorage.areFriends("Andrzej", "Przemek")

        self.assertEqual(result, "Andrzej is not friend Przemek")

    def test_get_friends_list(self):
        objectFriend = FriendShips()
        objectFriend.dict = {"Przemek": ["Ala", "Basia", "Piotrek"]}
        objectFriend.getFriendsList = MagicMock()
        objectFriend.getFriendsList.return_value = ["Ala", "Basia", "Piotrek"]

        objectStorage = FriendStorage()
        objectStorage.storage = objectFriend
        result = objectStorage.getFriendsList("Przemek")

        self.assertEqual(result, ["Ala", "Basia", "Piotrek"])

    def test_get_friends_list_lack_person(self):
        objectFriend = FriendShips()
        objectFriend.dict = {"Przemek": ["Ala", "Basia", "Piotrek"]}
        objectFriend.areFriends = MagicMock()
        objectFriend.areFriends.side_effect = Exception("This person not exist")

        objectStorage = FriendStorage()
        objectStorage.storage = objectFriend
        result = objectStorage.getFriendsList

        self.assertRaisesRegex(Exception, "This person not exist", result, "Adam")

    def test_make_friends(self):
        objectStorage = FriendStorage()
        objectStorage.storage = MagicMock()
        objectStorage.makeFriends("Maciek", "Bartek")
        objectStorage.storage.makeFriends.assert_called_with("Maciek", "Bartek")

    def test_make_friends_add_friend(self):
        objectFriend = FriendShips()
        objectFriend.dict = {"Przemek": ["Ala"]}
        objectFriend.makeFriends = MagicMock()
        objectFriend.makeFriends.return_value = {"Przemek": ["Ala", "Bartek"], "Bartek": ["Przemek"]}

        objectStorage = FriendStorage()
        objectStorage.storage = objectFriend
        result = objectStorage.makeFriends("Przemek", "Bartek")

        self.assertEqual(result, {"Przemek": ["Ala", "Bartek"], "Bartek": ["Przemek"]})
        objectStorage.storage.makeFriends.assert_called_with("Przemek", "Bartek")

    def test_make_friend_bad_type(self):
        objectFriend = FriendShips()
        objectFriend.makeFriends = MagicMock()
        objectFriend.makeFriends.side_effect = TypeError("People have to be type string")

        objectStorage = FriendStorage()
        objectStorage.storage = objectFriend
        result = objectStorage.makeFriends

        self.assertRaisesRegex(TypeError, "People have to be type string", result, "Maciek", False)


if __name__ == '__main__':
    main()
