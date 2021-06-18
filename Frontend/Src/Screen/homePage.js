import React, { useState, useEffect, useCallback } from 'react';
import {
	View,
	Image,
	Text,
	SafeAreaView,
	StyleSheet,
	Dimensions,
	TouchableHighlight,
	ScrollView
} from 'react-native';

import {
	createMaterialTopTabNavigator
} from '@react-navigation/material-top-tabs';

import axiosInstance, {
	baseURL
} from "../Context/Axios";

import {
	stack_navigate
} from '../Context/NavigationRoot';

import {
	ListItem
} from 'react-native-elements';

import {
	key_set,
	fulldate_of_date
} from "../Context/MyTool"


import FarmInfo from './FarmInfo'
import ProductionList from "./Productions"
const tab = createMaterialTopTabNavigator();

function homePageScreen(props) {
	// stack_navigate("CreateSensor", {field_id:1})
	const [farm, setFarm] = useState({});
	const [productions, setProductions] = useState();

	return (
		<tab.Navigator>
			<tab.Screen name="Nông trại">
				{() => <FarmInfo {...props} data={{ farm, setFarm }} />}
			</tab.Screen>
			<tab.Screen name="Sản phẩm" component={Productions} />
		</tab.Navigator>
	)
}

const Your_fame = (props) => {
	const { farm, setFarm } = props.data
	useEffect(
		() => {
			if (!farm["id"]) {
				(axiosInstance.get("api/farm/").then(resp => {
					setFarm(resp.data)
				}))
			}
		}
	)

	return (
		<SafeAreaView>
			<ScrollView style={styles.container}>

				<View style={styles.image_container}>
					<Image source={{ uri: baseURL + farm["farm_image"] }}
						style={{ width: 200, height: 200 }} />
				</View>

				<View style={styles.datas_container}>
					{
						Object.keys(farm).map((key, index) => {
							const exclude = ["farm_image", "id"]

							if (exclude.indexOf(key) == -1)
								return (
									< ListItem key={index} bottomDivider topDivider style={styles.data_container}>
										<ListItem.Title key={100 + index} style={styles.data_title}>{key_set[key]}</ListItem.Title>
										<ListItem.Subtitle key={200 + index} style={styles.data_subtitle}>{farm[key]}</ListItem.Subtitle>
									</ListItem>
								)

						})
					}
				</View>

				<View style={styles.button_container}>
					<TouchableHighlight
						style={styles.button}
						onPress={() => { }}
					>
						<Text style={styles.innerbtn}>Edit</Text>
					</TouchableHighlight>
					<TouchableHighlight
						style={styles.button}
						onPress={() => { props.navigation.navigate("ListFieldsScreen", {...props}) }}
					>
						<Text style={styles.innerbtn}>Fields</Text>
					</TouchableHighlight>

				</View>

			</ScrollView>
		</SafeAreaView >
	)

}

// get production from server .......
// TODO


// TODO
const Productions = () => {
	return (
		<ProductionList />
	)
}

const width = Dimensions.get("window").width;
const height = Dimensions.get("window").height;

const styles = StyleSheet.create({
	container: {
		backgroundColor: '#FBFDFE',
		width: width,
		height: (height),
		// backgroundColor: "red",
	},
	image_container: {
		flex: 1,
		// height: 200,
		alignItems: "center",
		justifyContent: "center"
	},
	datas_container: {
		flex: 1,
		// height: 400,
		// backgroundColor:"red"
	},
	data_container: {
		// flex: 8,
		// height: 70,

		// backgroundColor:"red"
	},
	data_title: {
		flex: 1
	},
	data_subtitle: {

	},
	button_container: {
		flex: 1,
		flexDirection: 'row',
		// backgroundColor: "coral",
		justifyContent: "space-evenly",
		alignItems: "center"
	},
	button: {
		borderRadius: 20,
		height: 40,
		width: 150,
		alignSelf: 'center',
		backgroundColor: '#9A79FE',
		paddingLeft: 20,
		paddingRight: 20,
		marginTop: 20,
		justifyContent: 'center',
		textAlign: 'center',
		flexDirection: 'row',
		// flex: 1
	},

	image: {
		height: 200,
		resizeMode: 'contain',
		justifyContent: 'center',
		alignSelf: 'center',
		marginTop: 50
	},
	textline: {
		margin: 10,
		marginLeft: 20
	},
	title: {
		fontWeight: 'bold',
		fontSize: 20,
	},
	text_content: {
		fontSize: 20
	},

	innerbtn: {
		color: '#FFF',
		fontSize: 18,
		alignSelf: 'center'
	},
	production_item: {
		margin: 20,
		backgroundColor: "#FFFFFF"
	}
})


export default homePageScreen;