"""Validate public metadata without network access or third-party dependencies."""
import json
from pathlib import Path
from urllib.parse import urlsplit


def validate():
    data = json.loads(Path(__file__).with_name('models.json').read_text(encoding='utf-8'))
    assert data['schema_version'] == 1
    assert isinstance(data['catalog_version'], int) and data['catalog_version'] > 0
    assert data['product'] == 'PixBatch'
    adapters = {'apiyi_all_prompt_v1', 'apiyi_vip_size_v1', 'apiyi_vip_quality_v1'}
    for provider in data['providers']:
        assert provider['id'] == 'apiyi_openai_compatible'
        assert provider['base_url'] == 'https://api.apiyi.com/v1'
        names = [model['id'] for model in provider['models']]
        assert len(names) == len(set(names)) and provider['default_model'] in names
        for model in provider['models']:
            assert model['adapter'] in adapters
            assert model['status'] in {'active', 'deprecated', 'disabled'}
            assert urlsplit(model['documentation']).hostname == 'docs.apiyi.com'
            assert model['size_presets']
            for preset in model['size_presets']:
                if model['size_control'] == 'prompt':
                    assert preset['prompt_prefix'] and preset['exact_dimensions_guaranteed'] is False
                    dimensions = (preset['expected_width'], preset['expected_height'])
                else:
                    assert model['size_control'] == 'size'
                    dimensions = (preset['width'], preset['height'])
                assert all(isinstance(n, int) and 0 < n <= 8192 for n in dimensions)
    print('Model catalog validation: PASS')


if __name__ == '__main__':
    validate()
