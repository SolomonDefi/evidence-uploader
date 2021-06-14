import { createRouter, createWebHistory } from 'vue-router';
import Home from '/src/views/Home.vue';
import SelectMethod from '/src/views/SelectMethod.vue';
import ExternalLink from '/src/views/ExternalLink.vue';
import SolomonLink from '/src/views/SolomonLink.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: { title: 'Solomon Evidence' },
    },
    {
      path: '/select/:type(buyer|merchant)',
      name: 'select',
      component: SelectMethod,
      meta: { title: 'Evidence Method' },
    },
    {
      path: '/upload-external/:type(buyer|merchant)',
      name: 'upload-external',
      component: ExternalLink,
      meta: { title: 'External Link' },
    },
    {
      path: '/upload-solomon/:type(buyer|merchant)',
      name: 'upload-solomon',
      component: SolomonLink,
      meta: { title: 'Solomon Link' },
    },
  ],
});

router.afterEach((to, _from) => {
  const parentTitle = to.matched.some(record => record.meta.title);
  document.title = to.meta.title || parentTitle || 'Solomon Evidence';
});

export default router;
