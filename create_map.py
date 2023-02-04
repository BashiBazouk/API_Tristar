def create_Map(latitude_list, longitude_list, name_list, text_list):
    # function to create map with stations and info hovering on them

    mapbox_access_token = open("mapbox_token").read()
    # https://stackoverflow.com/questions/42753745/how-can-i-parse-geojson-with-python

    fig = go.Figure()

    fig.add_trace(go.Scattermapbox(
        lat=latitude_list,
        lon=longitude_list,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=17,
            color='rgb(255, 0 , 0)',
            opacity=0.7
        ),
        text=name_list,
        hoverinfo='text'
    ))

    fig.add_trace(go.Scattermapbox(
        lat=latitude_list,
        lon=longitude_list,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=8,
            color='rgb(242, 177, 172)',
            opacity=0.7
        ),
        text=text_list,
        hoverinfo='text'
    ))

    fig.update_layout(
        title='Air Pollution Stations',
        autosize=True,
        hovermode='closest',
        showlegend=True,
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=53,
                lon=-8
            ),
            pitch=0,
            zoom=3,
            style='light'
        ),
    )
    fig.show()