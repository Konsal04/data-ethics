import numpy as np
import unittest

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


def aggregate_threat_score(departments):
    total_score = 0
    total_importance = 0
    for dept in departments:
        users_scores = dept['scores']
        importance = dept['importance']

        avg_score = np.mean(users_scores) if len(users_scores) > 0 else 0

        total_score += avg_score * importance
        total_importance += importance

    return min(90, max(0, total_score / total_importance))


class TestThreatScoreAggregation(unittest.TestCase):

    def test_aggregate_score_basic_functionality(self):
        departments = [
            {'scores': generate_random_data(30, 10, 50), 'importance': 3},
            {'scores': generate_random_data(32, 10, 50), 'importance': 3},
            {'scores': generate_random_data(35, 10, 50), 'importance': 3}
        ]
        score = aggregate_threat_score(departments)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 90)

    def test_aggregate_with_high_importance(self):
        departments = [
            {'scores': generate_random_data(10, 5, 50), 'importance': 1},
            {'scores': generate_random_data(80, 5, 50), 'importance': 5}
        ]
        score = aggregate_threat_score(departments)
        self.assertGreaterEqual(score, 50)

    def test_aggregate_with_low_importance_high_score(self):
        departments = [
            {'scores': generate_random_data(10, 5, 50), 'importance': 5},
            {'scores': generate_random_data(80, 5, 50), 'importance': 1}
        ]
        score = aggregate_threat_score(departments)
        self.assertLessEqual(score, 40)

    def test_large_variance_between_departments(self):
        departments = [
            {'scores': generate_random_data(5, 2, 100), 'importance': 1},
            {'scores': generate_random_data(80, 5, 200), 'importance': 5},
            {'scores': generate_random_data(60, 10, 150), 'importance': 3}
        ]
        score = aggregate_threat_score(departments)
        self.assertGreaterEqual(score, 40)
        self.assertLessEqual(score, 90)

    def test_no_users(self):
        departments = [
            {'scores': [], 'importance': 3},
            {'scores': generate_random_data(30, 10, 50), 'importance': 3}
        ]
        score = aggregate_threat_score(departments)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 90)

    def test_single_department_high_score(self):
        departments = [
            {'scores': generate_random_data(85, 2, 200), 'importance': 5}
        ]
        score = aggregate_threat_score(departments)
        self.assertAlmostEqual(score, 85, delta=1)

    def test_all_departments_low_threat(self):
        departments = [
            {'scores': generate_random_data(5, 3, 100), 'importance': 2},
            {'scores': generate_random_data(6, 2, 120), 'importance': 2},
            {'scores': generate_random_data(7, 2, 80), 'importance': 1}
        ]
        score = aggregate_threat_score(departments)
        self.assertLessEqual(score, 10)


if __name__ == '__main__':
    unittest.main()
