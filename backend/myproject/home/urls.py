# myproject/home/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('run_frequency_test/', views.run_frequency_test, name='run_frequency_test'),
    path('run_frequency_block_test/', views.run_frequency_block_test, name='run_frequency_block_test'),
    path('run_runs_test/', views.run_runs_test, name='run_runs_test'),
    path('run_longest_one_block_test/', views.run_longest_one_block_test, name='run_longest_one_block_test'),
    path('run_approximate_entropy_test/',views.run_approximate_entropy_test, name='run_approximate_entropy_test'),
    path('run_linear_complexity_test/',views.run_linear_complexity_test, name='run_linear_test'),
    path('run_non_overlapping_test/',views.run_non_overlapping_test, name='run_non_overlapping_test'),
    path('run_overlapping_test/',views.run_overlapping_test, name='run_overlapping_test'),
    path('run_statistical_test/',views.run_statistical_test, name='run_statistical_test'),
    path('run_serial_test/',views.run_serial_test, name='run_serial_test'),
    path('run_cumulative_sums_test/',views.run_cumulative_sums_test, name='run_cumulative_sums_test'),
    path('random_excursions_test/',views.run_random_excursions_test, name='run_random_excursions_test'),
    path('random_excursions_variant_test/',views.random_excursions_variant_test, name='random_excursions_variant_test'),
    path('run_binary_matrix_rank_text/',views.run_binary_matrix_rank_text, name='run_binary_matrix_rank_test'),
    path('run_spectral_test/',views.run_spectral_test, name='run_spectral_test'),
]
