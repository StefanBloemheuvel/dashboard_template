from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash
import pages_plugin

app = Dash(__name__, plugins=[pages_plugin])


dash.register_page('another_page', layout='Another page', path='/another-page')
dash.register_page('and_again', layout='And again!', path='/and-again')


app.layout = html.Div([
	dbc.NavbarSimple([
		dbc.NavItem(dbc.NavLink(page['name'], href=page['path'])) for page in dash.page_registry]),
    dash.page_container,
    
	html.H1('App Frame'),

	html.Div(
		dcc.Link('Go back home', href=dash.page_registry['pages.home']['path'])
	),

	html.Div([
		html.Div(dcc.Link(
			f"{page['name']} - {page['path']}",
			href=page['path']
		))
		for page in dash.page_registry.values()
		if page['module'] != 'pages.not_found_404'
	]),
			
	pages_plugin.page_container

])



if __name__ == '__main__':
	app.run_server(debug=True)

