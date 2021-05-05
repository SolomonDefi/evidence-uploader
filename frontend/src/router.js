import { createRouter, createWebHistory } from 'vue-router';
import Home from '/src/views/Home.vue';
import SelectMethod from '/src/views/SelectMethod.vue';
import ExternalLink from '/src/views/ExternalLink.vue';

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
      meta: { title: 'Evidence Method' },
    },
  ],
});

router.afterEach((to, _from) => {
  const parentTitle = to.matched.some(record => record.meta.title);
  document.title = to.meta.title || parentTitle || 'Solomon Evidence';
});

export default router;
