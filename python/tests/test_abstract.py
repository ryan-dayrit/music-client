import pytest
from unittest.mock import Mock
from music.repository.abstract import AbstractRepository


class TestAbstractRepository:
    """Test suite for the AbstractRepository abstract base class"""

    def test_abstract_repository_is_abstract(self):
        """Test that AbstractRepository cannot be instantiated directly"""
        with pytest.raises(TypeError):
            AbstractRepository({})

    def test_abstract_repository_requires_get_albums_implementation(self):
        """Test that subclasses must implement get_albums method"""
        
        # Create a subclass that doesn't implement get_albums
        class IncompleteRepository(AbstractRepository):
            pass
        
        with pytest.raises(TypeError):
            IncompleteRepository({})

    def test_abstract_repository_with_valid_implementation(self):
        """Test that a valid implementation can be instantiated"""
        
        # Create a valid subclass
        class ValidRepository(AbstractRepository):
            def get_albums(self):
                return []
        
        config = {'key': 'value'}
        repo = ValidRepository(config)
        assert repo._config == config
        assert repo.get_albums() == []

    def test_abstract_repository_stores_config(self):
        """Test that AbstractRepository stores configuration"""
        
        class TestRepository(AbstractRepository):
            def get_albums(self):
                return []
        
        config = {'host': 'localhost', 'port': 5432}
        repo = TestRepository(config)
        assert repo._config == config

    def test_abstract_repository_get_albums_is_abstract_method(self):
        """Test that get_albums is marked as an abstract method"""
        from abc import abstractmethod
        import inspect
        
        # Check that get_albums has the abstractmethod decorator
        method = getattr(AbstractRepository, 'get_albums')
        assert hasattr(method, '__isabstractmethod__')
        assert method.__isabstractmethod__

    def test_concrete_implementation_can_override_get_albums(self):
        """Test that concrete implementations can provide get_albums"""
        
        class ConcreteRepository(AbstractRepository):
            def get_albums(self):
                return [{'id': 1, 'title': 'Test Album'}]
        
        repo = ConcreteRepository({})
        albums = repo.get_albums()
        assert len(albums) == 1
        assert albums[0]['id'] == 1
        assert albums[0]['title'] == 'Test Album'

    def test_multiple_implementations_can_exist(self):
        """Test that multiple implementations can coexist"""
        
        class RepoA(AbstractRepository):
            def get_albums(self):
                return ['Album A']
        
        class RepoB(AbstractRepository):
            def get_albums(self):
                return ['Album B1', 'Album B2']
        
        repo_a = RepoA({})
        repo_b = RepoB({})
        
        assert repo_a.get_albums() == ['Album A']
        assert repo_b.get_albums() == ['Album B1', 'Album B2']
