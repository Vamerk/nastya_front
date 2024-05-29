import flet as ft
from datetime import date, datetime
import asyncio
import requests


# Replace with your actual API endpoint
API_BASE_URL = "http://localhost:8000"

def main(page: ft.Page):
    page.title = "Dispatch Tracker"

    date_input = ft.TextField(
        label="Date (YYYY-MM-DD)",
        value=date.today().strftime("%Y-%m-%d"),
    )

    dispatches_view = ft.ListView(expand=True)
    longest_dispatch_view = ft.Column(expand=True)

    async def fetch_dispatches(e):
        dispatch_date = datetime.strptime(date_input.value, "%Y-%m-%d").date()
        dispatches_view.controls.clear()
        longest_dispatch_view.controls.clear()

        # Fetch dispatches for the selected date
        async def fetch_data():
            response = requests.get(f"{API_BASE_URL}/dispatches/{dispatch_date.isoformat()}")
            if response.status_code == 200:  # Check status code
                dispatches = response.json()
                for dispatch in dispatches:
                    dispatches_view.controls.append(
                        ft.Card(
                            content=ft.Column(
                                [
                                    ft.Text(f"Call ID: {dispatch['call_id']}"),
                                    ft.Text(f"Dispatch Time: {dispatch['dispatch_time']}"),
                                    ft.Text(f"Brigade Number: {dispatch['brigade_number']}"),
                                    ft.Text(f"Measures Taken: {dispatch['measures_taken']}")
                                ]
                            )
                        )
                    )
                # Fetch the longest dispatch
                response = requests.get(f"{API_BASE_URL}/longest_dispatch/{dispatch_date.isoformat()}")
                if response.status_code == 200:
                    longest_dispatch = response.json()
                    longest_dispatch_view.controls.append(
                        ft.Card(
                            content=ft.Column(
                                [
                                    ft.Text(f"Call ID: {longest_dispatch['call_id']}"),
                                    ft.Text(f"Dispatch Time: {longest_dispatch['dispatch_time']}"),
                                    ft.Text(f"Arrival Time: {longest_dispatch['arrival_time']}"),
                                    ft.Text(f"Duration: {longest_dispatch['duration']}"),
                                    ft.Text(f"Brigade Number: {longest_dispatch['brigade_number']}"),
                                    ft.Text(f"Measures Taken: {longest_dispatch['measures_taken']}")
                                ]
                            )
                        )
                    )
            else:
                dispatches_view.controls.append(
                    ft.Text(f"Error fetching data. Status code: {response.status_code}")
                )

        await fetch_data()
        page.update()

    fetch_dispatches_button = ft.ElevatedButton(
        text="Fetch Dispatches",
        on_click=fetch_dispatches,
    )

    page.add(
        ft.Row(
            [
                date_input,
                fetch_dispatches_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.Container(
                    width=400,
                    content=ft.Column(
                        [
                            ft.Text("Dispatches"),
                            dispatches_view,
                        ],
                        expand=True,
                    ),
                ),
                ft.Container(
                    width=400,
                    content=ft.Column(
                        [
                            ft.Text("Longest Dispatch"),
                            longest_dispatch_view,
                        ],
                        expand=True,
                    ),
                ),
            ],
            expand=True,
        ),
    )

ft.app(target=main)