import React from 'react'
import { DrawerContentScrollView, DrawerItemList, DrawerItem } from '@react-navigation/drawer'
import { logout } from "../Context/AsyncStorage"
export default function CustomDrawerContent(props) {

    return (
        <DrawerContentScrollView {...props}>
            <DrawerItem
                label="Home"
                onPress={() => {
                    props.navigation.navigate("HomePageScreen", {})
                }}
            />
            <DrawerItem
                label="Fields"
                onPress={() => {
                    props.navigation.navigate("ListFieldsScreen", {})
                }}
            />
            <DrawerItem
                label="Log out"
                onPress={() => {
                    logout().then(data => {
                        if (data) {
                            props.navigation.navigate("UserLoginScreen", {})
                        }
                    })
                }}
            />

        </DrawerContentScrollView>
    );
}